
import string
import getpass

def check_password(password):

    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters (A-Z).")

    # Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters (a-z).")

    # Check numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add numbers (0-9).")

    # Check special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add special characters (!, @, #, etc.).")

    # Determine password strength
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, suggestions


# Main program
print("================================")
print("     PASSWORD STRENGTH ANALYZER")
print("================================")

password = getpass.getpass("Enter your password: ")

strength, suggestions = check_password(password)

print("\nPassword Strength:", strength)

if suggestions:
    print("\nSuggestions to improve your password:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("\nExcellent! All basic security checks passed.")

print("\nThank you for using Password Strength Analyzer!")
