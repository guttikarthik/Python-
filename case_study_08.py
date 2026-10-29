# Case Study 29: Password Policy Validation Engine

password_input = input("Enter candidate password: ")

has_minimum_length = len(password_input) >= 8
has_uppercase_letter = False
has_lowercase_letter = False
has_digit_number = False

for character in password_input:
    if character.isupper():
        has_uppercase_letter = True
    elif character.islower():
        has_lowercase_letter = True
    elif character.isdigit():
        has_digit_number = True

contains_common_word = False
if "password" in password_input.lower() or "1234" in password_input or "admin" in password_input.lower():
    contains_common_word = True

print("\n--- Password Security Audit ---")

if has_minimum_length:
    print("1. Minimum 8 characters  : PASS")
else:
    print("1. Minimum 8 characters  : FAIL (Too short)")

if has_uppercase_letter:
    print("2. Contains uppercase (A-Z): PASS")
else:
    print("2. Contains uppercase (A-Z): FAIL")

if has_lowercase_letter:
    print("3. Contains lowercase (a-z): PASS")
else:
    print("3. Contains lowercase (a-z): FAIL")

if has_digit_number:
    print("4. Contains digit (0-9)   : PASS")
else:
    print("4. Contains digit (0-9)   : FAIL")

if contains_common_word:
    print("5. No prohibited words   : FAIL (Found common word)")
else:
    print("5. No prohibited words   : PASS")

if has_minimum_length and has_uppercase_letter and has_lowercase_letter and has_digit_number and (not contains_common_word):
    print("\nResult: STRONG PASSWORD (Compliant with security policy)")
else:
    print("\nResult: WEAK PASSWORD (Rejected by policy engine)")
