import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  fetchAllRequirements,
  fetchRequirementById,
  fetchTestCaseMetadata,
} from "../services/requirementService";

const RequirementsPage = () => {
  const [requirements, setRequirements] = useState([]);
  const [selectedId, setSelectedId] = useState(null);
  const [requirementDetails, setRequirementDetails] = useState(null);
  const [testcaseStatus, setTestcaseStatus] = useState(null);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    fetchAllRequirements()
      .then(setRequirements)
      .catch(() => setError("Failed to load requirements."));
  }, []);

  const handleSelect = async (id) => {
    setSelectedId(id);
    try {
      const [reqDetail, status] = await Promise.all([
        fetchRequirementById(id),
        fetchTestCaseMetadata(id),
      ]);
      setRequirementDetails(reqDetail);
      setTestcaseStatus(status.testcase_generation_status);
    } catch {
      setError("Failed to load requirement details.");
    }
  };

  const handleGenerate = () => {
    navigate(`/requirements/${selectedId}/test-cases`); // generation handled there
  };

  const handleView = () => {
    navigate(`/requirements/${selectedId}/test-cases`);
  };

  return (
    <div className="flex h-full">
      {/* Sidebar */}
      <aside className="w-1/4 border-r p-4 overflow-y-auto">
        <h2 className="font-semibold text-lg mb-2">Requirements</h2>
        {requirements.map((req) => (
          <div
            key={req.requirement_id}
            onClick={() => handleSelect(req.requirement_id)}
            className={`cursor-pointer p-2 rounded mb-1 ${
              selectedId === req.requirement_id ? "bg-blue-100" : "hover:bg-gray-100"
            }`}
          >
            {req.title}
          </div>
        ))}
      </aside>

      {/* Main Panel */}
      <main className="flex-1 p-6 overflow-y-auto">
        {error && <p className="text-red-600 mb-2">{error}</p>}
        {requirementDetails && (
          <>
            <h2 className="text-xl font-semibold mb-2">{requirementDetails.title}</h2>
            <p className="mb-2 text-sm text-gray-500">Source: {requirementDetails.source_type}</p>
            <div className="mb-4">
              <h3 className="font-semibold">Raw Text:</h3>
              <p className="whitespace-pre-wrap">{requirementDetails.raw_text}</p>
            </div>

            <div className="space-x-4">
              {(testcaseStatus === "not_started" || testcaseStatus === "failed") && (
                <button
                  onClick={handleGenerate}
                  className="bg-green-600 text-white px-4 py-2 rounded"
                >
                  Generate Test Cases
                </button>
              )}
              {testcaseStatus === "generated" && (
                <button
                  onClick={handleView}
                  className="bg-blue-600 text-white px-4 py-2 rounded"
                >
                  View Test Cases
                </button>
              )}
              {testcaseStatus === "generating" && (
                <button
                  disabled
                  className="bg-gray-400 text-white px-4 py-2 rounded"
                >
                  Generating...
                </button>
              )}
            </div>
          </>
        )}
      </main>
    </div>
  );
};

export default RequirementsPage;
