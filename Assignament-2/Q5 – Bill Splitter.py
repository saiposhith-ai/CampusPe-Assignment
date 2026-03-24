

try:

    subtotal = float(input("Enter total bill amount: ₹"))
    people = int(input("Number of people: "))
    tax_percent = float(input("Tax percentage: "))
    tip_percent = float(input("Tip percentage: "))

    if people <= 0:
        print("Number of people must be greater than 0.")
    elif subtotal < 0:
        print("Bill amount cannot be negative.")
    else:

        tax_amount = subtotal * tax_percent / 100
        after_tax = subtotal + tax_amount
        tip_amount = after_tax * tip_percent / 100
        total = after_tax + tip_amount
        per_person = total / people

        print("\n=== BILL BREAKDOWN ===")
        print(f"Subtotal: ₹{subtotal:.2f}")
        print(f"Tax ({tax_percent}%): ₹{tax_amount:.2f}")
        print(f"After tax: ₹{after_tax:.2f}")
        print(f"Tip ({tip_percent}%): ₹{tip_amount:.2f}")
        print(f"Total: ₹{total:.2f}")
        print(f"Per person: ₹{per_person:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values only.")