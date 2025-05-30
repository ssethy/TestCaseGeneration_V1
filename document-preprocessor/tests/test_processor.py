# tests/test_processor.py

import unittest
from unittest.mock import patch
from app.service.processor import process_document


class TestDocumentProcessor(unittest.TestCase):

    @patch("app.service.processor.parse_docx")
    def test_process_docx(self, mock_parse_docx):
        mock_parse_docx.return_value = "Title: Login Page\n1. User should be able to login."

        result = process_document("./sample.docx", "docx")

        self.assertNotIn("version", result)
        self.assertNotIn("requirement_id", result)
        self.assertIn("raw_text", result)
        self.assertTrue(len(result["sections"]) > 0)
        self.assertIn("title", result["sections"][0])
        self.assertIn("content", result["sections"][0])

    @patch("app.service.processor.parse_pdf")
    def test_process_pdf(self, mock_parse_pdf):
        mock_parse_pdf.return_value = "Section 1: Intro\nThe system shall allow login."

        result = process_document("./sample.pdf", "pdf")

        self.assertNotIn("version", result)
        self.assertNotIn("requirement_id", result)
        self.assertIn("raw_text", result)
        self.assertTrue(isinstance(result["sections"], list))

    @patch("app.service.processor.parse_image")
    def test_process_image(self, mock_parse_image):
        mock_parse_image.return_value = "Security:\n- Passwords must be hashed."

        result = process_document("./sample.jpg", "jpg")

        self.assertIn("sections", result)
        self.assertGreater(len(result["sections"]), 0)

    def test_unsupported_file_type(self):
        with self.assertRaises(ValueError) as context:
            process_document("sample.txt", "txt")
        self.assertIn("Unsupported file type", str(context.exception))

    def test_empty_parsed_content(self):
        with patch("app.service.processor.parse_docx", return_value=""):
            with self.assertRaises(ValueError) as context:
                process_document("empty.docx", "docx")
            self.assertIn("Parsed document is empty", str(context.exception))


if __name__ == "__main__":
    unittest.main()
