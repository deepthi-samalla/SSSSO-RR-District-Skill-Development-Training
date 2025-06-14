# Assignment: CLI args (very simple)
# Task: Use sys.argv to accept one word from the command line and print it back.

import sys

# sys.argv[1] gets the first word provided after the script name
print(f"You entered: '{sys.argv[1]}'")