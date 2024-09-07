import re

def assess_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    upper_case_criteria = any(char.isupper() for char in password)
    lower_case_criteria = any(char.islower() for char in password)
    number_criteria = any(char.isdigit() for char in password)
    special_char_criteria = bool(re.search(r'[@$!%*#?&]', password))

    # Count how many criteria are met
    score = sum([length_criteria, upper_case_criteria, lower_case_criteria, number_criteria, special_char_criteria])

    # Provide feedback based on the score
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    feedback = []
    if not length_criteria:
        feedback.append("- Password should be at least 8 characters long.")
    if not upper_case_criteria:
        feedback.append("- Password should contain at least one uppercase letter.")
    if not lower_case_criteria:
        feedback.append("- Password should contain at least one lowercase letter.")
    if not number_criteria:
        feedback.append("- Password should contain at least one number.")
    if not special_char_criteria:
        feedback.append("- Password should contain at least one special character (@, $, !, %, *, #, ?, &).")
    
    # Print strength and feedback
    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(suggestion)

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")
    assess_password_strength(password)

if __name__ == "__main__":
    main()
