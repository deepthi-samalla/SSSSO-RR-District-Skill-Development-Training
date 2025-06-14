# Assignment: Pylint basics
# Task: Create a script with one variable named badly (like X) and run pylint to see the warning.
# (This is Version 1: With a "badly" named variable)

# A variable with a single uppercase letter name (which Pylint typically warns about)
X = 10

print(f"The value of X is: {X}")

# Assignment: Pylint basics
# Task: Rename it to follow lowercase_style and rerun pylint.
# (This is Version 2: With a "good" named variable)

# Renaming 'X' to a Pylint-friendly lowercase_style name
my_variable = 10

print(f"The value of my_variable is: {my_variable}")

X = 5
print(X)