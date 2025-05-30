import axios from "axios";

// Fetch test cases for a specific requirement
export const fetchTestCases = async (requirementId) => {
  const response = await axios.get(`/api/requirements/${requirementId}/test-cases`);
  return response.data;
};

// Trigger test case generation
export const generateTestCases = async (requirementId) => {
  const response = await axios.post("/api/test-cases/generate", {
    requirement_id: requirementId,
  });
  return response.data;
};

export const compareTestCases = async ({ requirement_id, from_version, to_version }) => {
  const response = await axios.post("/api/test-cases/compare", {
    requirement_id,
    from_version,
    to_version,
  });
  return response.data;
};