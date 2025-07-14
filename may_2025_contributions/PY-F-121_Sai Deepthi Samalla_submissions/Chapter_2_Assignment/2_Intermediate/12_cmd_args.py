# Chapter 2 - Intermediate Assignment 2: Command Line Arguments with sys.argv
# Question: Use the command line to run a script and pass arguments using sys.argv.

import sys

print("--- Script Started ---")

# Print the entire sys.argv list
print(f"All arguments received: {sys.argv}")

# Check if any arguments were provided beyond the script name
if len(sys.argv) > 1:
    print(f"The script name is: {sys.argv[0]}")
    print(f"The first argument is: {sys.argv[1]}")

    # If there's a second argument, print it too
    if len(sys.argv) > 2:
        print(f"The second argument is: {sys.argv[2]}")
else:
    print("No additional arguments were provided to the script.")

print("--- Script Finished ---")