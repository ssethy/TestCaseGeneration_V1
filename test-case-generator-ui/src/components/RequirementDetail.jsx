import React from "react";

const RequirementDetail = ({
  requirement,
  testcaseStatus,
  onGenerate,
  onView,
}) => {
  if (!requirement) return null;

  return (
    <div className="flex-1 p-6 overflow-y-auto">
      <h2 className="text-xl font-semibold mb-2">{requirement.title}</h2>
      <p className="mb-2 text-sm text-gray-500">
        Source Type: {requirement.source_type}
      </p>

      <div className="mb-4">
        <h3 className="font-semibold mb-1">Raw Text:</h3>
        <p className="whitespace-pre-wrap border rounded p-3 bg-gray-50">
          {requirement.raw_text}
        </p>
      </div>

      <div className="space-x-4">
        {(testcaseStatus === "not_started" || testcaseStatus === "failed") && (
          <button
            onClick={onGenerate}
            className="bg-green-600 text-white px-4 py-2 rounded"
          >
            Generate Test Cases
          </button>
        )}
        {testcaseStatus === "generated" && (
          <button
            onClick={onView}
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
    </div>
  );
};

export default RequirementDetail;
