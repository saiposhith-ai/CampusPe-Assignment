
def count_words(text):
    return len(text.split())

def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

def count_consonants(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in vowels:
            count += 1
    return count

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def longest_word(text):
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)

def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print(f"Words: {count_words(text)}")
    print(f"Vowels: {count_vowels(text)}")
    print(f"Consonants: {count_consonants(text)}")
    print(f"Reversed: {reverse_text(text)}")
    print(f"Palindrome: {'Yes' if is_palindrome(text) else 'No'}")
    print(f"Without vowels: {remove_vowels(text)}")

    longest = longest_word(text)
    if longest:
        print(f"Longest word: {longest} ({len(longest)} letters)")
    else:
        print("Longest word: None")

    freq = word_frequency(text)
    print("Word Frequency:")
    for word, count in freq.items():
        print(f"{word}: {count}")



try:
    user_input = input("Enter text: ").strip()

    if not user_input:
        print("Input cannot be empty.")
    else:
        analyze_text(user_input)

except Exception:
    print("An error occurred during processing.")