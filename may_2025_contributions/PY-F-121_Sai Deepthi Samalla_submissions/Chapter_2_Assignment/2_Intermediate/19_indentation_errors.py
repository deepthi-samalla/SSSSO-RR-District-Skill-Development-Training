# Chapter 2 - Intermediate Assignment 9: Incorrect Indentation and Correction
# Question: Write a script that contains incorrect indentation. Then correct it and explain the changes.

"""def greet_user(name):
print(f"Hello, {name}!") # This line has incorrect indentation
    print("Welcome to the program.") # This line also has incorrect indentation

def calculate_sum(a, b):
    total = a + b
  return total # This line has incorrect indentation

# Calling the functions
greet_user("Alice")
sum_result = calculate_sum(10, 20)
print(f"The sum is: {sum_result}")"""


# This script demonstrates correct indentation after fixing errors.

def greet_user(name):
    # Corrected: This line now has 4 spaces of indentation, aligning it with the standard.
    print(f"Hello, {name}!")
    # Corrected: This line also has 4 spaces of indentation, consistent with the block.
    print("Welcome to the program.")

def calculate_sum(a, b):
    # This line was already correctly indented.
    total = a + b
    # Corrected: This line now has 4 spaces of indentation, aligning it with the block.
    return total

# Calling the functions (these lines were already at the correct top-level indentation)
greet_user("Alice")
sum_result = calculate_sum(10, 20)
print(f"The sum is: {sum_result}")