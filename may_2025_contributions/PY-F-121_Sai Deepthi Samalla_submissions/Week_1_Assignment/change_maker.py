# Assignment: Numeric operators & change-maker
# Task: Change for < 100 rupees.

amount = int(input("Enter amount in rupees (less than 100): "))
print(f"For ₹{amount}:\nYou need {amount // 50} x ₹50 notes\nAnd {(amount % 50) // 10} x ₹10 coins")