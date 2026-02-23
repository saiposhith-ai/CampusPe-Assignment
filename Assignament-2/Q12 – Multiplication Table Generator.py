# Q12 – Multiplication Table Generator (Bonus Version)

try:
    while True:
        print("\n=== MULTIPLICATION TABLE GENERATOR ===")
        print("1. Generate table for a single number")
        print("2. Generate full 1–10 multiplication grid")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        # Option 1 – Single Number Table
        if choice == "1":
            number = int(input("Enter number: "))
            range_end = int(input("Enter range (end): "))

            if range_end <= 0:
                print("Range must be greater than 0.")
            else:
                print(f"\nMultiplication Table of {number}\n")
                for i in range(1, range_end + 1):
                    print(f"{number} x {i} = {number * i}")

        # Option 2 – Full 1–10 Grid
        elif choice == "2":
            print("\n=== FULL MULTIPLICATION TABLE (1–10) ===\n")

            # Header row
            print("     ", end="")
            for i in range(1, 11):
                print(f"{i:4}", end="")
            print("\n" + "-" * 50)

            # Table body
            for i in range(1, 11):
                print(f"{i:2} |", end=" ")
                for j in range(1, 11):
                    print(f"{i*j:4}", end="")
                print()

        # Exit
        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please select 1-3.")

except ValueError:
    print("Invalid input! Please enter numeric values only.")