import React from "react";

const renderTestCase = (tc) => (
  <div key={tc.id} className="border rounded p-3 mb-2 bg-white shadow-sm text-sm">
    <p className="font-semibold mb-1">{tc.title} (ID: {tc.id})</p>
    <div className="mb-1">
      <span className="font-medium">Steps:</span>
      <ul className="list-disc list-inside ml-4">
        {tc.steps.map((step, i) => (
          <li key={i}>{step}</li>
        ))}
      </ul>
    </div>
    <div>
      <span className="font-medium">Expected:</span> {tc.expected_result}
    </div>
  </div>
);

const DiffViewer = ({ added = [], removed = [], modified = [], unchanged = [] }) => {
  return (
    <div className="space-y-6">
      {added.length > 0 && (
        <section>
          <h2 className="text-green-600 font-bold text-lg mb-2">🟢 Added</h2>
          {added.map(renderTestCase)}
        </section>
      )}
      {removed.length > 0 && (
        <section>
          <h2 className="text-red-600 font-bold text-lg mb-2">🔴 Removed</h2>
          {removed.map(renderTestCase)}
        </section>
      )}
      {modified.length > 0 && (
        <section>
          <h2 className="text-yellow-600 font-bold text-lg mb-2">🟠 Modified</h2>
          {modified.map(renderTestCase)}
        </section>
      )}
      {unchanged.length > 0 && (
        <section>
          <h2 className="text-gray-500 font-bold text-lg mb-2">⚪ Unchanged</h2>
          {unchanged.map(renderTestCase)}
        </section>
      )}
    </div>
  );
};

export default DiffViewer;
