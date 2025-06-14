# Assignment: Boolean type
# Task: Store 0, '', and 42 in a list. Loop through the list and print whether each element is truthy or falsy.

# Create the list with the specified values (and a few more for good measure)
data_list = [0, '', 42]

# Loop through each item in the list
for item in data_list:
    # Check if the item is truthy or falsy using an if/else statement
    # In Python, an 'if' statement directly evaluates the truthiness of a value.
    if item: # If 'item' is truthy (e.g., 42)
        print(f"The value '{item}' is Truthy.")
    else:    # If 'item' is falsy (e.g., 0, '')
        print(f"The value '{item}' is Falsy.")