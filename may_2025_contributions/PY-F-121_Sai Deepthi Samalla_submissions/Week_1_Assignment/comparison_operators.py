# Assignment: Comparison operators
# Task: Input an age and print True if the person is at least 18, otherwise False.

# Get age input from the user and convert it to an integer
age = int(input("Please enter your age: "))

# Use a comparison operator (>=) to check if the age is 18 or more.
# The result of this check (True or False) is stored in 'is_adult'.
is_adult = (age >= 18)

# Print the result clearly.
print(f"Is the person at least 18 years old? {is_adult}")