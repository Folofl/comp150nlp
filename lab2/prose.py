# Assignment: Lab2
# By:         Alena Borisenko 
# Created:    September 25th, 2017
# Submitted:  September 26th, 2017

import operator
import nltk
import re

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

from nltk.corpus import gutenberg
gutenberg.fileids()
['austen-emma.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt']

def remove_bad_words(target_list):
    bad_vals = [',', '.', ';', "'", '-', '!', '?', '"', ',"']
    return [value for value in target_list if value not in bad_vals ] 

def make_ngram(n, source_sents):
    ngram = {}
    for sent in source_sents:
        for word_i in range(n - 1, len(sent)):
            key = ""
            for k in range (word_i - (n - 1), word_i):
                key += sent[k] + " "
            key += sent[word_i]
            if key in ngram:
                ngram[key] += 1
            else:
                ngram[key]  = 1
    ngram = sorted(ngram.items(), key=operator.itemgetter(1), reverse=True)
    return ngram

a1_sents = gutenberg.sents('austen-emma.txt')
a2_sents = gutenberg.sents('edgeworth-parents.txt')
a3_sents = gutenberg.sents('melville-moby_dick.txt')

a1 = []
a1_valid_word_count = 0;
a2 = []
a2_valid_word_count = 0;
a3 = []
a3_valid_word_count = 0;

for sent in a1_sents:
    valid_sent = remove_bad_words(sent)
    a1.append(valid_sent)
    a1_valid_word_count += len(valid_sent)
for sent in a2_sents:
    valid_sent = remove_bad_words(sent)
    a2.append(valid_sent)
    a2_valid_word_count += len(valid_sent)
for sent in a3_sents:
    valid_sent = remove_bad_words(sent)
    a3.append(valid_sent)
    a3_valid_word_count += len(valid_sent)


print("----a1")
print(a1_valid_word_count)

a1_unigram = make_ngram(1, a1)
for i in range (0, 10):
    print(a1_unigram[i])
print("----------")

a1_bigram  = make_ngram(2, a1)
for i in range (0, 10):
    print(a1_bigram[i])
print("----------")

a1_trigram = make_ngram(3, a1)
for i in range (0, 10):
    print(a1_trigram[i])
print("----------")

a1_trigram = make_ngram(3, a1)
for i in range (0, 10):
    print(a1_trigram[i])
print("----------")

a1_tetragram = make_ngram(4, a1)
for i in range (0, 10):
    print(a1_tetragram[i])
print("----------")


print("-a2")
print(a2_valid_word_count)

a2_unigram = make_ngram(1, a2)
for i in range (0, 10):
    print(a2_unigram[i])
print("----------")

a2_bigram  = make_ngram(2, a2)
for i in range (0, 10):
    print(a2_bigram[i])
print("----------")

a2_trigram = make_ngram(3, a2)
for i in range (0, 10):
    print(a2_trigram[i])
print("----------")


print("--a3")
print(a3_valid_word_count)

a3_unigram = make_ngram(1, a3)
for i in range (0, 10):
    print(a3_unigram[i])
print("----------")

a3_bigram  = make_ngram(2, a3)
for i in range (0, 10):
    print(a3_bigram[i])
print("----------")

a3_trigram = make_ngram(3, a3)
for i in range (0, 10):
    print(a3_trigram[i])
print("----------")
