# Assignment: Comparison + logical
# Task: Check if three numbers are in strictly increasing order.

# Get three integer inputs directly
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Use chained comparison for a concise check and print the result
print(f"Are the numbers in strictly increasing order? {num1 < num2 < num3}")
