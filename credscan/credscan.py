"""
Naively scans python code for credentials
"""


import tokenize
import re

from pylint.checkers import BaseTokenChecker
from pylint.interfaces import ITokenChecker, HIGH


class CredentialChecker(BaseTokenChecker):
    """
    Checks if any credentials exist as python strings
    """

    __implements__ = ITokenChecker

    name = 'password_detected'
    msgs = {'E9001': ('Password: `%s` detected in source file',
                      'password-detected',
                      'Do not include passwords in source files.'),
           }

    def process_tokens(self, tokens):
        """
        Processes each string token in the python code
        """
        for tok_type, token, (start_row, _), _, _ in tokens:
            if tok_type == tokenize.STRING:
                self._process_string_token(token, start_row)

    def _process_string_token(self, token, start_row):
        """
        Processes a single string token
        """
        if CredentialChecker._is_password(token):
            self.add_message('E9001', line=start_row, args=(token), confidence=HIGH)

    @staticmethod
    def _is_password(token):
        """
        Determines whether or not a string is a password.
        Any string without a space and with more than a single character class
        is considered a password.
        """
        if ' ' in token:
            return False

        character_classes = 0

        # Check for uppercase
        if re.search(r"[A-Z]", token) is not None:
            character_classes += 1

        # searching for lowercase
        if re.search(r"[a-z]", token) is not None:
            character_classes += 1

        # searching for symbols
        if re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', token) is not None:
            character_classes += 1

        if character_classes > 1:
            return True

        return False


def register(linter):
    """
    Register the credential checker linter
    """
    linter.register_checker(CredentialChecker(linter))
