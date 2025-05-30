import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { uploadRequirement } from "../services/requirementService";

const RequirementUploadPage = () => {
  const [file, setFile] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setError("");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file) {
      setError("Please select a file to upload.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      await uploadRequirement(formData);
      navigate("/requirements");
    } catch (err) {
      setError("Upload failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-xl mx-auto mt-12 p-6 bg-white rounded shadow">
      <h1 className="text-xl font-semibold mb-4">Upload Requirement Document</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="file"
          accept=".pdf,.docx,.png,.txt"
          onChange={handleFileChange}
          className="mb-4 block w-full border border-gray-300 p-2 rounded"
        />
        {error && <p className="text-red-600 mb-2">{error}</p>}
        <button
          type="submit"
          disabled={loading}
          className="px-4 py-2 bg-blue-600 text-white rounded disabled:opacity-50"
        >
          {loading ? "Uploading..." : "Submit"}
        </button>
      </form>
    </div>
  );
};

export default RequirementUploadPage;
