import React from "react";

const RequirementList = ({ requirements, selectedId, onSelect }) => {
  return (
    <aside className="w-1/4 border-r p-4 overflow-y-auto">
      <h2 className="font-semibold text-lg mb-2">Requirements</h2>
      {requirements.map((req) => (
        <div
          key={req.requirement_id}
          onClick={() => onSelect(req.requirement_id)}
          className={`cursor-pointer p-2 rounded mb-1 ${
            selectedId === req.requirement_id ? "bg-blue-100" : "hover:bg-gray-100"
          }`}
        >
          {req.title}
        </div>
      ))}
    </aside>
  );
};

export default RequirementList;
