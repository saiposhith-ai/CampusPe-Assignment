
from datetime import date

try:
    year = int(input("Enter birth year: "))
    month = int(input("Enter birth month (1-12): "))
    day = int(input("Enter birth day (1-31): "))

    birth_date = date(year, month, day)
    today = date.today()

    if birth_date > today:
        print("Birth date cannot be in the future.")
    else:
        age_days = (today - birth_date).days
        age_years = age_days // 365
        age_months = age_years * 12
        age_hours = age_days * 24
        age_minutes = age_hours * 60
        years_to_100 = 100 - age_years

        print("\n=== EXACT AGE DETAILS ===")
        print(f"Age in Years: {age_years}")
        print(f"Age in Days: {age_days}")
        print(f"Age in Hours: {age_hours}")
        print(f"Age in Minutes: {age_minutes}")
        print(f"Years until 100: {years_to_100 if years_to_100 > 0 else 'Already 100 or above!'}")

except ValueError:
    print("Invalid date entered!")