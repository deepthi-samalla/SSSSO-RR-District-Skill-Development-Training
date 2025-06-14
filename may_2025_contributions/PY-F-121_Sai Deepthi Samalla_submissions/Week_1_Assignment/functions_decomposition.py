# Assignment: Decomposition / functions
# Task: Write a function square(n) that returns n*n and call it for numbers 1–5, printing each result.

# Define the function 'square'
def square(n):
    return n * n

# Call the function for numbers 1 to 5 and print results directly
for num in range(1, 6):
    print(f"The square of {num} is: {square(num)}")