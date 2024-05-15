import re

def check_password_strength(password):
    length = len(password)
    score = 0

    if length >= 8:
        score += 1
    elif length >= 6:
        score += 0.5

    
    if re.search(r'[A-Z]', password):
        score += 1

    if re.search(r'[a-z]', password):
        score += 1

    if re.search(r'\d', password):
        score += 1

    if re.search(r'[\W_]', password):
        score += 1

    return score

def assess_password_strength(score):
    if score > 4:
        return "Very Strong"
    elif score > 3:
        return "Strong"
    elif score > 2:
        return "Moderate"
    elif score > 1:
        return "Weak"
    else:
        return "Very Weak"

def main():
    while True:
        password = input("Enter your password: ")
        strength_score = check_password_strength(password)
        strength_label = assess_password_strength(strength_score)
        print(f"Password Strength: {strength_label}")
        
        choice = input("Do you want to check another password? (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()
