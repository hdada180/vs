import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password is too short (less than 8 characters)."
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        return "Medium: Add both uppercase and lowercase letters."
    if not re.search("[0-9]", password):
        return "Medium: Add numbers to make it stronger."
    if not re.search("[@#$%^&*+=]", password):
        return "Good, but add special characters for maximum security."
    return "Strong: Excellent password!"

user_pass = input("Enter a password to check: ")
print(check_password_strength(user_pass))