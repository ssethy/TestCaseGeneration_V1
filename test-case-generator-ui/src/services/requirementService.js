import axios from "axios";

export const uploadRequirement = async (formData) => {
  try {
    const response = await axios.post("/api/upload", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    return response.data;
  } catch (error) {
    throw error;
  }
};

// Fetch all uploaded requirements
export const fetchAllRequirements = async () => {
  const response = await axios.get("/api/requirements");
  return response.data;
};

// Fetch full details of a specific requirement
export const fetchRequirementById = async (requirementId) => {
  const response = await axios.get(`/api/requirements/${requirementId}`);
  return response.data;
};

// Fetch test case generation metadata for a requirement
export const fetchTestCaseMetadata = async (requirementId) => {
  const response = await axios.get(`/api/requirements/${requirementId}/test-cases/metadata`);
  return response.data;
};