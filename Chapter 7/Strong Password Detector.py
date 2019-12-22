import re

def checkPasswordStrength(passwordString):
    """ Determines if a password is a strong password based on various criteria"""
    isStrongPassword = True
    regexLowerCaseChar = re.compile(r'[a-z]')
    regexUpperCaseChar = re.compile(r'[A-Z]')
    regexDigit = re.compile(r'\d+')

    if regexDigit.search(passwordString) is None:
        isStrongPassword = False
        print("A strong password must have at least one digit.")

    if regexUpperCaseChar.search(passwordString) is None:
        isStrongPassword = False
        print("A strong password must have at least one uppercase character.")

    if regexLowerCaseChar.search(passwordString) is None:
        isStrongPassword = False
        print("A strong password must have at least one lowercase character.")

    if len(passwordString) < 8:
        isStrongPassword = False
        print("A strong password must have at least 8 characters.")

    if isStrongPassword:
        print("Nice, the password is strong!")


checkPasswordStrength('abc123ABC')
checkPasswordStrength('1aA')
checkPasswordStrength('!@#$%^&*(')
