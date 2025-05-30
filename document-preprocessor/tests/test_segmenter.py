# tests/test_segmenter.py

import unittest
from app.utils.text_segmenter import segment_text

class TestTextSegmenter(unittest.TestCase):

    def test_basic_section_segmentation(self):
        raw_text = """
        Login Page Requirements:

        1. User should be able to login with email and password.
        2. System shall block account after 5 invalid attempts.

        Security Features:

        - Password must be encrypted.
        - OTP must expire after 5 minutes.
        """

        sections = segment_text(raw_text)
        self.assertEqual(len(sections), 2)
        self.assertEqual(sections[0]["title"], "Login Page Requirements:")
        self.assertIn("1. User should be able to login", sections[0]["content"])
        self.assertEqual(sections[1]["title"], "Security Features:")
        self.assertIn("- Password must be encrypted.", sections[1]["content"])

    def test_no_headers_present(self):
        raw_text = """
        This is a requirement specification with no headings.

        1. Feature A must be available.
        2. Feature B should support export.
        """

        sections = segment_text(raw_text)
        self.assertEqual(len(sections), 1)
