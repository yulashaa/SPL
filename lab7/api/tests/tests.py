import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))

import unittest
from api.utils.email_validator import EmailValidator

class TestEmailValidator(unittest.TestCase):
    def test_valid_email(self):
        valid_email = "test@example.com"
        self.assertTrue(EmailValidator.is_valid_email(valid_email))

    def test_invalid_email(self):
        invalid_email = "test12423@com"
        self.assertFalse(EmailValidator.is_valid_email(invalid_email))

if __name__ == "__main__":
    unittest.main()
