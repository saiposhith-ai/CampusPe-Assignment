# Q3 – String Manipulator

sentence = input("Enter a sentence: ").strip()

if not sentence:
    print("You entered an empty sentence.")
else:
    # Basic Calculations
    chars_with_space = len(sentence)
    chars_without_space = len(sentence.replace(" ", ""))
    words = sentence.split()
    word_count = len(words)

    # Transformations
    uppercase = sentence.upper()
    lowercase = sentence.lower()
    title_case = sentence.title()
    reversed_sentence = sentence[::-1]

    # First & Last Word
    first_word = words[0]
    last_word = words[-1]

    # Display Results
    print("\n=== STRING ANALYSIS ===")
    print(f"Original: {sentence}")
    print(f"Characters (with spaces): {chars_with_space}")
    print(f"Characters (without spaces): {chars_without_space}")
    print(f"Words: {word_count}")
    print(f"UPPERCASE: {uppercase}")
    print(f"lowercase: {lowercase}")
    print(f"Title Case: {title_case}")
    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")
    print(f"Reversed: {reversed_sentence}")