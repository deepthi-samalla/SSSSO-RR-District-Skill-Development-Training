from flask import Flask, render_template, request, url_for, redirect
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    
    error = None
    age_result = None
    next_birthday_info = None
    weekday_of_birth = None

    today = date.today()

    # When the user submits the form via a POST request
    if request.method == 'POST':
        birth_year_str = request.form.get('birth_year')
        birth_month_str = request.form.get('birth_month')
        birth_day_str = request.form.get('birth_day')

        try:
            # All inputs are converted to integers for validation
            birth_year = int(birth_year_str) if birth_year_str else None
            birth_month = int(birth_month_str) if birth_month_str else None
            birth_day = int(birth_day_str) if birth_day_str else None

            # Check if birth year is present and within a reasonable range
            if not birth_year:
                error = "Please enter your birth year."
            elif birth_year < 1900 or birth_year > today.year:
                error = "Please enter a valid birth year between 1900 and the current year."
            
            # Additional validation if month and day are provided
            if birth_month and (birth_month < 1 or birth_month > 12):
                error = "Month must be between 1 and 12."
            if birth_day and (birth_day < 1 or birth_day > 31):
                error = "Day must be between 1 and 31."

            # Construct the birth date object if all components are provided
            if birth_year and birth_month and birth_day:
                try:
                    birth_date = date(birth_year, birth_month, birth_day)
                except ValueError:
                    # This catches invalid date combinations like Feb 30th
                    error = "Please enter a valid date."

                # Check if the birth date is a future date
                if not error and birth_date > today:
                    error = "The birth date cannot be in the future."

            # If there are no errors, perform calculations
            if not error and birth_year:
                # Use a default date for calculation if month/day are missing
                if not birth_month or not birth_day:
                    # If month/day are missing, we still want a date to work with
                    birth_date = date(birth_year, 1, 1)
                
                # Calculate age using relativedelta for precise years, months, and days
                age = relativedelta(today, birth_date)
                age_result = {
                    'years': age.years,
                    'months': age.months,
                    'days': age.days,
                    # Calculate total hours for extra detail
                    'hours': int((today - birth_date).total_seconds() / 3600)
                }

                # --- Calculate time until next birthday ---
                next_birthday = date(today.year, birth_date.month, birth_date.day)
                # If the birthday has already passed this year, calculate for the next year
                if next_birthday < today:
                    next_birthday = date(today.year + 1, birth_date.month, birth_date.day)

                time_until_birthday = relativedelta(next_birthday, today)
                next_birthday_info = {
                    'months': time_until_birthday.months,
                    'days': time_until_birthday.days,
                }

                # --- Determine weekday of birth ---
                weekday_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                weekday_of_birth = weekday_name[birth_date.weekday()]

        except (ValueError, TypeError) as e:
            # Catches errors if the input is not a valid number
            error = "Invalid input. Please enter numbers for the date."
            print(f"Error during input processing: {e}")

    # Render the template with results, errors, or an empty form
    return render_template(
        'index.html',
        error=error,
        age_result=age_result,
        next_birthday_info=next_birthday_info,
        weekday_of_birth=weekday_of_birth,
        prev_year=request.form.get('birth_year', ''),
        prev_month=request.form.get('birth_month', ''),
        prev_day=request.form.get('birth_day', ''),
        date=date
    )

if __name__ == '__main__':
    # Running the app
    app.run(debug=True)
