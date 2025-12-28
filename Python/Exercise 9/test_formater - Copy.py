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

    def test_upper(self):
        test_text = "John ORaw"
        result = formatter.convert_upper(test_text)
        # Intentionally wrong expected value to force a failure
        self.assertEqual(result, "JoHN ORAW")

        )

    def test_convert_capital(self):
        self.assertEqual(
            formater.convert_capital("dUBLIN"),
            "Dublin"
        )


if __name__ == "__main__":
    unittest.main()
