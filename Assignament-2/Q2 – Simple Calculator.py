# Q2 – Simple Calculator

try:
    # Taking inputs
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nResults:")
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")

    # Division with zero handling
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2:.2f}")
        print(f"{num1} % {num2} = {num1 % num2}")
    else:
        print("Division and Modulus not possible (division by zero)")

    # Exponentiation
    print(f"{num1} ^ {num2} = {num1 ** num2}")

except ValueError:
    print("Invalid input! Please enter numeric values only.")