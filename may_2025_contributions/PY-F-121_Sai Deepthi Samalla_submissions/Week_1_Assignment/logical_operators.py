# Assignment: Logical operators
# Task: Read two Boolean values (e.g., True/False) and print the results of and, or, and not on them.

# Get the first boolean value from user input
# .lower() converts input to lowercase (e.g., "True" becomes "true")
# == 'true' checks if the lowercase input is exactly "true", resulting in True or False
bool1 = input("Enter the first boolean value (True/False): ").lower() == 'true'

# Get the second boolean value from user input
bool2 = input("Enter the second boolean value (True/False): ").lower() == 'true'

# Print the results of logical operations directly
print(f"Bool1 AND Bool2: {bool1 and bool2}")
print(f"Bool1 OR Bool2:  {bool1 or bool2}")
print(f"NOT Bool1:       {not bool1}")
print(f"NOT Bool2:       {not bool2}")