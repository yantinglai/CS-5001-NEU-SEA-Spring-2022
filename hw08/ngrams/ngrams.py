""""Ngrams controller file"""
import sys
from frequencies import NgramFrequencies  # 文件名字不能够和class 名字一样
from text_cleaner import TextCleaner

TOP = 10


def main(file_name):
    """Use TextCleaner to open and clean the text"""
    tc = TextCleaner(file_name)
    sentence_list = tc.open_file(file_name)

    unigrams = NgramFrequencies()
    bigrams = NgramFrequencies()
    trigrams = NgramFrequencies()

    # Make unigrams, bigrams, and trigrams
    for sentence in sentence_list:
        sentence = sentence.split(" ")
        sentence = [x for x in sentence if len(x) > 0]

        for i in range(len(sentence)):
            unigrams.add_item(sentence[i])
            if i < len(sentence) - 1:
                bigrams.add_item(sentence[i] + "_" + sentence[i+1])
            if i < len(sentence) - 2:
                trigrams.add_item(
                    sentence[i] + "_" + sentence[i+1] + "_" + sentence[i+2])

    print("\nTop 10 unigrams:")

    TOP = 10
    a = unigrams.top_n_freqs
    for i in range(TOP):
        print(a[i])

    print("\nTop 10 bigrams:")
    b = bigrams.top_n_freqs
    for i in range(TOP):
        print(b[i])

    print("\nTop 10 trigrams:")
    c = trigrams.top_n_freqs
    for i in range(TOP):
        print(c[i])


main(sys.argv[1])
