
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


try:

    num = int(input("Enter a number: "))

    if is_prime(num):
        print(f"{num} is a PRIME number.")
    else:
        print(f"{num} is NOT a prime number.")


    start = int(input("\nEnter start range: "))
    end = int(input("Enter end range: "))

    if start > end:
        print("Invalid range. Start must be less than or equal to end.")
    else:
        print(f"\nPrime numbers between {start} and {end}:")

        primes = []
        for number in range(start, end + 1):
            if is_prime(number):
                primes.append(str(number))

        if primes:
            print(", ".join(primes))
        else:
            print("No prime numbers found in this range.")

except ValueError:
    print("Invalid input! Please enter integers only.")