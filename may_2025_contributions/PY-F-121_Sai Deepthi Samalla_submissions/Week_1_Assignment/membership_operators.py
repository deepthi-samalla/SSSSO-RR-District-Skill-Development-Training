# Assignment: Membership operators
# Task: Ask the user for a letter and print whether that letter appears in the word "python".

# Get input from user and convert to lowercase for case-insensitive check
user_letter = input("Please enter a letter: ").lower()

# Check if the letter is in "python" and print the boolean result
print(f"Does '{user_letter}' appear in 'python'? {user_letter in 'python'}")