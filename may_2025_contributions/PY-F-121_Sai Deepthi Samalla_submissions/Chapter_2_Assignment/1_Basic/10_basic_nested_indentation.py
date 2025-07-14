# Chapter 2 - Basic Assignment 10: Nested Indentation.
# Question: Write a program with nested indentation that prints messages at different levels.

condition1 = True
condition2 = True

print("Start of program")

if condition1:
    print("    Inside first condition (Level 1)") # Indented 4 spaces
    if condition2:
        print("        Inside second condition (Level 2)") # Indented 8 spaces
    print("    Back to first condition (Level 1)") # Indented 4 spaces

print("End of program")