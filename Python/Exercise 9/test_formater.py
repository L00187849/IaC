"""
Unit tests for formater.py
"""

import unittest
import formater


class TestFormater(unittest.TestCase):
    """Test cases for string formatting functions."""

    def test_convert_lower(self):
        self.assertEqual(
            formater.convert_lower("John ORaw"),
            "john oraw"
        )

    def test_convert_upper(self):
        self.assertEqual(
            formater.convert_upper("John ORaw"),
            "JOHN ORAW"
        )

    def test_convert_capital(self):
        self.assertEqual(
            formater.convert_capital("dUBLIN"),
            "Dublin"
        )


if __name__ == "__main__":
    unittest.main()
