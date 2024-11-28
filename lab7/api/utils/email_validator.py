import re

class EmailValidator:
    EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    @staticmethod
    def is_valid_email(email):
        return re.match(EmailValidator.EMAIL_REGEX, email)