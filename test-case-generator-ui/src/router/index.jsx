import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";

import RequirementUploadPage from "../pages/RequirementUploadPage";
import RequirementsPage from "../pages/RequirementsPage";
import RequirementTestCasesPage from "../pages/RequirementTestCasesPage";
import CompareVersionsPage from "../pages/CompareVersionsPage";
import NotFoundPage from "../pages/NotFoundPage";

const AppRouter = () => (
  <Router>
    <Routes>
      <Route path="/" element={<Navigate to="/upload" replace />} />
      <Route path="/upload" element={<RequirementUploadPage />} />
      <Route path="/requirements" element={<RequirementsPage />} />
      <Route path="/requirements/:id/test-cases" element={<RequirementTestCasesPage />} />
      <Route path="/compare" element={<CompareVersionsPage />} />
      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  </Router>
);

export default AppRouter;
