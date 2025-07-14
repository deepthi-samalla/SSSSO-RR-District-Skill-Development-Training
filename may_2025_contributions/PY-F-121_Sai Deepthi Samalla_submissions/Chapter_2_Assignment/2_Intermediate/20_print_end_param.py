# Chapter 2 - Intermediate Assignment 10: Print Behavior with end Parameter (Short Version)
# Question: Compare and demonstrate how print behaves with and without end-line characters (end="").

print("--- Default print behavior ---")
print("Line 1")
print("Line 2")

print("\n--- Print behavior with end='' ---")
print("Line 1", end=" ") # No newline
print("Line 2", end=" ") # No newline
print("line 3")         # Default newline