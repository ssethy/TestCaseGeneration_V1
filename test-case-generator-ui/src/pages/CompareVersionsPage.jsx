import React, { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { compareTestCases } from "../services/testCaseService";
import DiffViewer from "../components/DiffViewer";

const CompareVersionsPage = () => {
  const [searchParams] = useSearchParams();
  const requirementId = searchParams.get("requirement_id");
  const fromVersion = searchParams.get("from_version");
  const toVersion = searchParams.get("to_version");

  const [diffResult, setDiffResult] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    if (requirementId && fromVersion && toVersion) {
      compareTestCases({ requirement_id: requirementId, from_version: fromVersion, to_version: toVersion })
        .then(setDiffResult)
        .catch(() => setError("Failed to compare test cases."));
    }
  }, [requirementId, fromVersion, toVersion]);

  return (
    <div className="p-6 max-w-6xl mx-auto">
      <h1 className="text-2xl font-semibold mb-4">Compare Test Case Versions</h1>
      {error && <p className="text-red-600 mb-4">{error}</p>}

      {!diffResult ? (
        <p>Loading...</p>
      ) : (
        <DiffViewer
          added={diffResult.added}
          removed={diffResult.removed}
          modified={diffResult.modified}
          unchanged={diffResult.unchanged}
        />
      )}
    </div>
  );
};

export default CompareVersionsPage;
