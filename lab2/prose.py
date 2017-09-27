# Assignment: Lab2
# By:         Alena Borisenko 
# Created:    September 25th, 2017
# Submitted:  September 26th, 2017

import operator
import nltk
#nltk.download('punkt')
from nltk.corpus import gutenberg
gutenberg.fileids()
['austen-emma.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt']

austen    = gutenberg.sents('austen-emma.txt')
edgeworth = gutenberg.words('edgeworth-parents.txt')
melville  = gutenberg.words('melville-moby_dick.txt')

a_unigram = {}
a_bigram  = {}

# go through every word
for j in austen:
    for i in j:
        if i in a_unigram:
            a_unigram[i] += 1
        else:
            a_unigram[i] = 1

a_unigram = sorted(a_unigram.items(), key=operator.itemgetter(1), reverse=True)

print(a_unigram[0])
print(a_unigram[1])
print(a_unigram[2])

for j in austen:
    for i in range(1, len(j)):
        two_words = j[i - 1] + " " + j[i]
        if two_words in a_bigram:
            a_bigram[two_words] += 1
        else:
            a_bigram[two_words] = 1

a_bigram = sorted(a_bigram.items(), key=operator.itemgetter(1), reverse=True)

print(a_bigram[0])
print(a_bigram[1])
print(a_bigram[2])