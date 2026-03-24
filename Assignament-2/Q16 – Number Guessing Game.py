
import random

best_score = None

while True:
    secret_number = random.randint(1, 100)
    attempts_left = 7
    attempts_used = 0

    print("\n=== NUMBER GUESSING GAME ===")
    print("Guess the number between 1 and 100")
    print("You have 7 attempts.\n")

    while attempts_left > 0:
        try:
            guess = int(input("Enter your guess: "))
            attempts_used += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts_used} attempts.")

          
                if best_score is None or attempts_used < best_score:
                    best_score = attempts_used
                    print("🏆 New Best Score!")

                break

            elif guess > secret_number:
                print("Too High!")

            else:
                print("Too Low!")

            if abs(guess - secret_number) <= 5:
                print("🔥 Very Close!")

            attempts_left -= 1
            print(f"Attempts remaining: {attempts_left}\n")

        except ValueError:
            print("Invalid input! Enter an integer.")

    else:
        print(f"❌ You lost! The number was {secret_number}.")

    if best_score:
        print(f"Best Score so far: {best_score} attempts")

    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thank you for playing!")
        break