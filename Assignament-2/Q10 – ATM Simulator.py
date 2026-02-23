# Enhanced ATM Simulator with Bonus Features

balance = 10000
correct_pin = "1234"
transaction_history = []
transaction_count = 0

# PIN Authentication (3 Attempts)
attempts = 3
while attempts > 0:
    entered_pin = input("Enter your 4-digit PIN: ")
    if entered_pin == correct_pin:
        print("PIN verified successfully.\n")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. Attempts remaining: {attempts}")

if attempts == 0:
    print("Too many incorrect attempts. Card blocked.")
else:

    while True:
        print("\n=== ATM MENU ===")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # Check Balance
        if choice == "1":
            print(f"Current Balance: ₹{balance:.2f}")

        # Deposit
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                if amount <= 0:
                    print("Deposit amount must be greater than 0.")
                else:
                    balance += amount
                    transaction_count += 1
                    transaction_history.append(f"Deposited ₹{amount:.2f}")
                    print("Deposit successful!")
                    print(f"New Balance: ₹{balance:.2f}")
            except ValueError:
                print("Invalid amount entered.")

        # Withdraw
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                if amount <= 0:
                    print("Withdrawal amount must be greater than 0.")
                elif amount > balance:
                    print("Insufficient balance.")
                elif balance - amount < 500:
                    print("Minimum balance of ₹500 must be maintained.")
                else:
                    balance -= amount
                    transaction_count += 1
                    transaction_history.append(f"Withdrew ₹{amount:.2f}")
                    print("Withdrawal successful!")
                    print(f"New Balance: ₹{balance:.2f}")
            except ValueError:
                print("Invalid amount entered.")

        # Mini Statement
        elif choice == "4":
            print("\n=== MINI STATEMENT ===")
            if transaction_count == 0:
                print("No transactions yet.")
            else:
                for i, transaction in enumerate(transaction_history, start=1):
                    print(f"{i}. {transaction}")
                print(f"\nTotal Transactions: {transaction_count}")
            print(f"Available Balance: ₹{balance:.2f}")

        # Exit
        elif choice == "5":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice! Please select between 1-5.")