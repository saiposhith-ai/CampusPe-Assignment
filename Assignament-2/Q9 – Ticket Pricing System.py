
try:
    age = int(input("Enter age: "))
    day = input("Enter day of week: ").strip().lower()
    tickets = int(input("Enter number of tickets: "))

    if tickets <= 0:
        print("Number of tickets must be greater than 0.")
    elif age < 0:
        print("Age cannot be negative.")
    else:

        if age < 3:
            base_price = 0
            category = "Free"
        elif 3 <= age <= 12:
            base_price = 150
            category = "Child"
        elif 13 <= age <= 59:
            base_price = 300
            category = "Adult"
        else:
            base_price = 200
            category = "Senior"

        weekend_days = ["friday", "saturday", "sunday"]

        if day in weekend_days:
            discount_percent = 20
        else:
            discount_percent = 0

        discount_amount = base_price * discount_percent / 100
        final_price_per_ticket = base_price - discount_amount
        total_amount = final_price_per_ticket * tickets


        print("\n=== TICKET BILL ===")
        print(f"Category: {category}")
        print(f"Base Price per Ticket: ₹{base_price:.2f}")
        print(f"Discount: {discount_percent}%")
        print(f"Discount Amount per Ticket: ₹{discount_amount:.2f}")
        print(f"Final Price per Ticket: ₹{final_price_per_ticket:.2f}")
        print(f"Total Amount: ₹{total_amount:.2f}")

except ValueError:
    print("Invalid input! Please enter correct numeric values.")