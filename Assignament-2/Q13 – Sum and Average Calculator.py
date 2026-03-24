
import statistics

try:
    count = int(input("How many numbers? "))

    if count <= 0:
        print("Count must be greater than 0.")
    else:
        numbers = []

        for i in range(1, count + 1):
            num = float(input(f"Enter number {i}: "))
            numbers.append(num)

        total = sum(numbers)
        average = total / count
        maximum = max(numbers)
        minimum = min(numbers)
        median = statistics.median(numbers)

        try:
            mode = statistics.mode(numbers)
        except statistics.StatisticsError:
            mode = "No unique mode"

        print("\n=== STATISTICAL RESULTS ===")
        print(f"Sum: {total}")
        print(f"Average: {average:.2f}")
        print(f"Maximum: {maximum}")
        print(f"Minimum: {minimum}")
        print(f"Median: {median}")
        print(f"Mode: {mode}")

except ValueError:
    print("Invalid input! Please enter numeric values only.")