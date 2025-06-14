# Assignment: Indentation
# Task: Use a for loop to print a 5-row left-aligned triangle of * characters (1 on the first row, 5 on the last).

# Loop from 1 to 5 (inclusive) for each row
for row_number in range(1, 6):
    # Print asterisks, with the count equal to the current row_number
    print('*' * row_number)