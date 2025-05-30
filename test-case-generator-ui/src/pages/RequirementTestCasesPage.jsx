import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import {
  fetchTestCases,
  generateTestCases,
} from "../services/testCaseService";

const RequirementTestCasesPage = () => {
  const { id } = useParams();
  const [testCases, setTestCases] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    loadTestCases();
  }, [id]);

  const loadTestCases = async () => {
    try {
      setLoading(true);
      const data = await fetchTestCases(id);
      setTestCases(data);
    } catch {
      setError("Failed to load test cases.");
    } finally {
      setLoading(false);
    }
  };

  const handleRegenerate = async () => {
    try {
      setLoading(true);
      await generateTestCases(id);
      await loadTestCases(); // refresh after regeneration
    } catch {
      setError("Regeneration failed.");
    } finally {
      setLoading(false);
    }
  };

  const handleDownload = (type) => {
    // Placeholder for download logic
    alert(`Download as ${type} not implemented`);
  };

  const handleCompare = () => {
    navigate("/compare");
  };

  return (
    <div className="p-6 max-w-5xl mx-auto">
      <h1 className="text-2xl font-semibold mb-4">Generated Test Cases</h1>
      {error && <p className="text-red-600 mb-4">{error}</p>}
      {loading ? (
        <p>Loading...</p>
      ) : (
        <>
          <table className="w-full border mb-4 text-sm">
            <thead className="bg-gray-200">
              <tr>
                <th className="border px-2 py-1">ID</th>
                <th className="border px-2 py-1">Title</th>
                <th className="border px-2 py-1">Steps</th>
                <th className="border px-2 py-1">Expected Result</th>
              </tr>
            </thead>
            <tbody>
              {testCases.map((tc) => (
                <tr key={tc.id}>
                  <td className="border px-2 py-1">{tc.id}</td>
                  <td className="border px-2 py-1">{tc.title}</td>
                  <td className="border px-2 py-1">
                    <ul className="list-disc list-inside">
                      {tc.steps.map((step, i) => (
                        <li key={i}>{step}</li>
                      ))}
                    </ul>
                  </td>
                  <td className="border px-2 py-1">{tc.expected_result}</td>
                </tr>
              ))}
            </tbody>
          </table>

          <div className="space-x-4">
            <button
              onClick={handleRegenerate}
              className="bg-yellow-600 text-white px-4 py-2 rounded"
            >
              Regenerate Test Cases
            </button>
            <button
              onClick={() => handleDownload("csv")}
              className="bg-gray-600 text-white px-4 py-2 rounded"
            >
              Download CSV
            </button>
            <button
              onClick={() => handleDownload("json")}
              className="bg-gray-600 text-white px-4 py-2 rounded"
            >
              Download JSON
            </button>
            <button
              onClick={handleCompare}
              className="bg-blue-600 text-white px-4 py-2 rounded"
            >
              Compare Versions
            </button>
          </div>
        </>
      )}
    </div>
  );
};

export default RequirementTestCasesPage;
