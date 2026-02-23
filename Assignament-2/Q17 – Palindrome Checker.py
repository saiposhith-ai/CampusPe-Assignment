

try:
    user_input = input("Enter word/number: ").strip()

    if not user_input:
        print("Input cannot be empty.")
    else:
  
        original = user_input
        cleaned = user_input.lower()

        reversed_text = cleaned[::-1]

        print("\n=== PALINDROME CHECK ===")
        print(f"Original: {original}")
        print(f"Reversed: {original[::-1]}")

        if cleaned == reversed_text:
            print("Result: PALINDROME")
        else:
            print("Result: NOT A PALINDROME")

except Exception as e:
    print("An unexpected error occurred.")