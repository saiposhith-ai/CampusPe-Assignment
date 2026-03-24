
def factorial(n):
    if n < 0:
        return "Not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result



def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    if n <= 0:
        return "Enter positive integer"
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a



def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))



def reverse_number(n):
    sign = -1 if n < 0 else 1
    reversed_num = int(str(abs(n))[::-1])
    return sign * reversed_num



def is_armstrong(n):
    digits = str(abs(n))
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == abs(n)



def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


# 8. LCM
def lcm(a, b):
    return abs(a * b) // gcd(a, b)



def is_perfect_number(n):
    if n <= 1:
        return False
    total = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i
    return total == n



def math_menu():
    while True:
        print("\n=== NUMBER SYSTEM MENU ===")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        try:
            if choice == "1":
                n = int(input("Enter number: "))
                print("Result:", factorial(n))

            elif choice == "2":
                n = int(input("Enter number: "))
                print("Prime:" if is_prime(n) else "Not Prime")

            elif choice == "3":
                n = int(input("Enter position (n): "))
                print("Fibonacci:", fibonacci(n))

            elif choice == "4":
                n = int(input("Enter number: "))
                print("Sum of digits:", sum_of_digits(n))

            elif choice == "5":
                n = int(input("Enter number: "))
                print("Reversed number:", reverse_number(n))

            elif choice == "6":
                n = int(input("Enter number: "))
                print("Armstrong:" if is_armstrong(n) else "Not Armstrong")

            elif choice == "7":
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("GCD:", gcd(a, b))

            elif choice == "8":
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("LCM:", lcm(a, b))

            elif choice == "9":
                n = int(input("Enter number: "))
                print("Perfect Number:" if is_perfect_number(n) else "Not Perfect")

            elif choice == "10":
                print("Exiting program...")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Invalid input! Please enter integers only.")


math_menu()