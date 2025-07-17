import datetime

def calculate_age():
    """
    Calculates a person's age given their birth date.
    The program asks for birth year (and optionally month/day) and computes the current age
    using the datetime module. It also includes extensions for exact age, weekday of birth,
    time until next birthday, and input validation.
    """
    print("Welcome to the Age Calculator!")

    # 1. Get Current Date
    current_date = datetime.date.today()
    print(f"Current Date: {current_date.strftime('%Y-%m-%d')}")

    # --- Get User Input for Birth Date ---
    # Birth Year (Mandatory) with Validation
    while True:
        try:
            birth_year_str = input("Enter your birth year (e.g., 1990): ")
            birth_year = int(birth_year_str)
            if birth_year <= 0:
                print("Birth year must be a positive number.")
            elif birth_year > current_date.year:
                print("Birth year cannot be in the future. Please try again.")
            else:
                break # Valid year entered
        except ValueError:
            print("Invalid input. Please enter a whole number for the year.")

    # Birth Month and Day (Optional)
    birth_month = 1  # Default to January
    birth_day = 1    # Default to 1st
    full_date_provided = False

    while True:
        choice = input("Do you want to enter your birth month and day for a more precise age calculation? (yes/no): ").lower().strip()
        if choice in ['yes', 'y']:
            full_date_provided = True
            # Get Month with Validation
            while True:
                try:
                    birth_month_str = input("Enter your birth month (1-12): ")
                    birth_month = int(birth_month_str)
                    if 1 <= birth_month <= 12:
                        break # Valid month entered
                    else:
                        print("Invalid month. Please enter a number between 1 and 12.")
                except ValueError:
                    print("Invalid input. Please enter a whole number for the month.")

            # Get Day with Validation
            while True:
                try:
                    birth_day_str = input("Enter your birth day (1-31): ")
                    birth_day = int(birth_day_str)
                    # Basic check for day; more robust validation will happen when creating datetime.date object
                    if 1 <= birth_day <= 31:
                        break # Valid day entered
                    else:
                        print("Invalid day. Please enter a number between 1 and 31.")
                except ValueError:
                    print("Invalid input. Please enter a whole number for the day.")
            break # Exit month/day choice loop
        elif choice in ['no', 'n']:
            print("Proceeding with year-only calculation for approximation.")
            break # Exit month/day choice loop
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")

    # 2. Construct Birth Date and Validate (Extension: Validate input - no future dates, valid day/month combos)
    try:
        birth_date = datetime.date(birth_year, birth_month, birth_day)
    except ValueError as e:
        # This catches errors like February 30th, April 31st, etc.
        print(f"\nError: Could not create a valid date with the provided input. {e}")
        print("This typically happens for invalid day/month combinations (e.g., February 30th, April 31st).")
        print("Please restart the program and enter valid date components.")
        return # Exit the function if the date is invalid

    # Final check for future dates after full date construction (important if month/day were entered)
    if birth_date > current_date:
        print("\nError: Your birth date cannot be in the future! Please check your input.")
        return

    print(f"Your Birth Date: {birth_date.strftime('%Y-%m-%d')}")

    # 3. Calculate Age (Initial calculation for years)
    age_years = current_date.year - birth_date.year

    # Adjust if the birthday hasn't occurred yet this year
    # Compares (current_month, current_day) with (birth_month, birth_day)
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age_years -= 1

    print(f"\nYour age is: {age_years} years.")

    # --- Possible Extensions ---

    if full_date_provided:
        # Calculate exact age in years, months, days
        # This logic handles month and day rollovers for precise calculation.
        age_months = current_date.month - birth_date.month
        age_days = current_date.day - birth_date.day

        if age_days < 0:
            # If current day is before birth day, we "borrow" days from the previous month.
            # Calculate the number of days in the month *before* the current month.
            # Example: current_date is July 14, birth_date is June 20.
            # We need days from June (30 days).
            # (current_date.replace(day=1) - datetime.timedelta(days=1)) gives the last day of the previous month.
            last_day_of_prev_month = (current_date.replace(day=1) - datetime.timedelta(days=1)).day
            age_days = last_day_of_prev_month - birth_date.day + current_date.day
            age_months -= 1 # Adjust month because we borrowed days

        if age_months < 0:
            # If current month is before birth month, we "borrow" months from the previous year.
            age_months += 12 # Add 12 months to make it positive
            age_years -= 1   # Adjust year because we borrowed months

        print(f"Your exact age is: {age_years} years, {age_months} months, and {age_days} days.")

        # Determine weekday of birth (Extension)
        birth_weekday = birth_date.strftime("%A") # %A gives full weekday name (e.g., "Monday")
        print(f"You were born on a {birth_weekday}.")

        # Time until next birthday (Extension)
        next_birthday_year = current_date.year
        # If the birthday has already passed this year, the next one is in the next calendar year.
        if (current_date.month, current_date.day) > (birth_date.month, birth_date.day):
            next_birthday_year += 1

        try:
            # Attempt to create the next birthday date
            next_birthday = datetime.date(next_birthday_year, birth_date.month, birth_date.day)
            days_until_next_birthday = (next_birthday - current_date).days

            if days_until_next_birthday == 0:
                print("🥳 Happy Birthday! Today is your birthday!")
            else:
                print(f"There are {days_until_next_birthday} days until your next birthday.")
        except ValueError:
            # Special handling for February 29th birthdays on non-leap years
            if birth_month == 2 and birth_day == 29:
                print("Special case: Your birthday is February 29th. Calculating the next birthday on a non-leap year might require more complex logic.")
                print("For a full calculation of such edge cases, consider using `dateutil.relativedelta` library.")
            else:
                print("Could not determine days until next birthday due to an unexpected date error.")


# This block ensures that the calculate_age() function is called only when
# the script is executed directly (e.g., `python Age_Calculator.py`),
# and not when it's imported as a module into another script.
if __name__ == "__main__":
    calculate_age()
