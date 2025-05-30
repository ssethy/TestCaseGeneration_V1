import React from "react";

const TestCaseTable = ({ testCases }) => {
  if (!testCases || testCases.length === 0) {
    return <p>No test cases found.</p>;
  }

  return (
    <table className="w-full border text-sm mb-4">
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
  );
};

export default TestCaseTable;
