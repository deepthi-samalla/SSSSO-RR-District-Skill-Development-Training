# Assignment: Identity operators
# Task: Create two identical lists a = [1,2] and b = [1,2]. Print the results of a is b and a == b.

# Create two identical lists
a = [1, 2]
b = [1, 2]

# Print the results of identity (is) and equality (==) comparisons
print(f"a is b: {a is b}")     # Checks if they are the exact same object in memory
print(f"a == b: {a == b}")     # Checks if they have the same value