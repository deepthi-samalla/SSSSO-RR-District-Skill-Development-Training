# Chapter 2 - Basic Assignment 8: Line Continuation
# Question: Use line continuation (\) to split a long expression over two lines.

# A long mathematical expression split using line continuation (\)
# Note: The backslash must be the very last character on the line.
result = 100 + 200 * 3 / 6 - \
         (50 + 25) * 2

print(f"The result of the long calculation is: {result}")

# You can also implicitly continue lines within parentheses, brackets, or braces,
# but the backslash is explicit for general expressions.
long_message = ("This is a very long message that " +
                "I am splitting across multiple lines " +
                "for better readability without a backslash."
)
print(long_message)