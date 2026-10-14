text_input = input("Enter a sentence or a line of text: ")
word_modifier = input("Enter a word you want to remove or highlight: ")
censor = "[REDACTED]"

word_true = modifier_word.lower() in text_input.lower()
word_count = text_input.lower().count(modifier_word.lower())
censored_text = text_input.replace(modifier_word, censor)

print("\n--- Results ---")
print(f"Original Text: '{text_input}'")
print(f"Target Word: '{modifier_word}'")
print(f"Does the word exist in the text?: {word_exists}")
print(f"Number of occurrences: {word_count}")
print(f"Modified text: {censored_text}")
