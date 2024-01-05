def count_words(sentence):
    words = sentence.split()
    return len(words)


given_sentence = "Write a Python function to count the number of words"
word_count = count_words(given_sentence)

print(f"The number of words in the sentence is: {word_count}")
