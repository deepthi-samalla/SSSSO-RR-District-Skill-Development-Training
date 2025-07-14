# Chapter 2 - Intermediate Assignment 7: Line Continuation Character
# Question: Use a continuation character to break a mathematical expression that spans more than 80 characters.

# This is a very long mathematical expression, broken into multiple lines
# using the backslash (\) character for explicit line continuation.
# Without the backslash, Python would see the new line as the end of the statement.
result = 10 + 20 + 30 + 40 + 50 + 60 + 70 + 80 + 90 + 100 + \
         110 + 120 + 130 + 140 + 150 + 160 + 170 + 180 + 190 + \
         200 + 210 + 220 + 230 + 240 + 250 + 260 + 270 + 280

print(f"The result of the long mathematical expression is: {result}")