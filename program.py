text_input = input("Enter a sentence or a line of text: ")
word_modifier = input("Enter a word you want to remove or highlight: ")
censor = "[REDACTED]"

word_true = modifier_word.lower() in text_input.lower()
word_count = text_input.lower().count(word_modifier.lower())
censored_text = text_input.replace(word_modifier, censor)

print("\n--- Results ---")
print(f"Original Text: '{text_input}'")
print(f"Target Word: '{word_modifier}'")
print(f"Was the word present?: {word_true}")
print(f"Number of occurrences: {word_count}")
print(f"Modified text: {censored_text}")
