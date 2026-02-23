# Q8 – Leap Year Checker

try:
    year = int(input("Enter a year: "))

    if year <= 0:
        print("Year must be a positive number.")

    else:
        print(f"\nChecking year: {year}")

        if year % 400 == 0:
            print(f"{year} is a LEAP year.")
            print("Reason: It is divisible by 400.")

        elif year % 100 == 0:
            print(f"{year} is NOT a leap year.")
            print("Reason: It is divisible by 100 but not by 400.")

        elif year % 4 == 0:
            print(f"{year} is a LEAP year.")
            print("Reason: It is divisible by 4 but not by 100.")

        else:
            print(f"{year} is NOT a leap year.")
            print("Reason: It is not divisible by 4.")

except ValueError:
    print("Invalid input! Please enter a valid year.")