# tests/test_routes.py

import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestPreprocessRoute(unittest.TestCase):

    @patch("app.service.processor.parse_docx")
    def test_post_preprocess_docx(self, mock_parse_docx):
        mock_parse_docx.return_value = (
            "Login Page\n1. User should be able to login.\n2. System shall lock after 5 failures."
        )

        response = client.post(
            "/preprocess/",
            json={"file_path": "./sample.docx", "file_type": "docx"}
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertNotIn("version", data)
        self.assertNotIn("requirement_id", data)
        self.assertTrue(len(data["sections"]) > 0)
        self.assertIn("title", data["sections"][0])
        self.assertIn("content", data["sections"][0])

    def test_invalid_file_type(self):
        response = client.post(
            "/preprocess/",
            json={"file_path": "./sample.txt", "file_type": "txt"}
        )
        self.assertEqual(response.status_code, 422)  # Enum validation by Pydantic

    def test_missing_fields(self):
        response = client.post(
            "/preprocess/",
            json={"file_type": "docx"}  # file_path missing
        )
        self.assertEqual(response.status_code, 422)

    @patch("app.service.processor.parse_pdf", return_value="")
    def test_empty_content_error(self, _):
        response = client.post(
            "/preprocess/",
            json={"file_path": "./empty.pdf", "file_type": "pdf"}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("Parsed document is empty", response.json()["detail"])

if __name__ == "__main__":
    unittest.main()
