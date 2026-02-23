# Q14 – Factorial Calculator

try:
    n = int(input("Enter a number: "))

    if n < 0:
        print("Factorial is not defined for negative numbers.")

    elif n == 0:
        print("0! = 1")

    else:
        factorial = 1
        steps = ""

        for i in range(n, 0, -1):
            factorial *= i
            steps += str(i)
            if i != 1:
                steps += " × "

        print(f"\n{n}! = {steps} = {factorial}")

except ValueError:
    print("Invalid input! Please enter an integer.")