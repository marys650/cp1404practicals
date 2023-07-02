"""
Word Occurrences
Estimate: 30 minutes
Actual:   45 minutes
"""


def format_word(word_count):
    max_word_length = max(len(word) for word in word_count)
    for word, count in sorted(word_count.items()):
        print(f"{word:>{max_word_length}} : {count}")


def main():
    sentence = input("Enter the sentence: ")
    word_count = {}
    words = sentence.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    format_word(word_count)


main()
