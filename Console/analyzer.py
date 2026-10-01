print("=== Sentence Analyzer ===")

sentence = input("Enter a sentence: ")

# Counters
char_count = len(sentence)
letter_count = 0
digit_count = 0
space_count = 0 
upper_count = 0
lower_count = 0

# Analyze characters
for character in sentence:
    if character.isalpha():
        letter_count += 1 # letter_count = letter_count + 1 (shorthand)

    if character.isdigit():
        digit_count += 1

    if character.isspace():
        space_count += 1

    if character.isupper():
        upper_count += 1

    if character.islower():
        lower_count += 1


# Analyze words
words = sentence.split()
word_count = len(words)

# Find longest word
if words:
    longest_word = max(words, key=len)
else:
    longest_word = ""


# Display results
print("\n--- Analysis ---")
print(f"Characters: {char_count}")
print(f"Words: {word_count}")
print(f"Letters: {letter_count}")
print(f"Digits: {digit_count}")
print(f"Spaces: {space_count}")
print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
print(f"Longest word: {longest_word}")