# Assignment: Lab2
# By:         Alena Borisenko 
# Created:    September 25th, 2017
# Submitted:  September 26th, 2017

import operator
import nltk
import re
nltk.download('punkt')
from nltk.corpus import gutenberg
gutenberg.fileids()
['austen-emma.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt']

def remove_bad_words(target_list):
    bad_vals = [',', '.', ';', "'", '-', '!', '?', '"', ',"']
    return [value for value in target_list if value not in bad_vals ] 

def make_ngram(n, source_sents):
    ngram = {}
    for j in source_sents:
        for i in range(n - 1, len(j)):
            key = ""
            for k in range (i - (n - 1), i):
                key += j[k] + " "
            key += j[i]
            if key in ngram:
                ngram[key] += 1
            else:
                ngram[key]  = 1
    ngram = sorted(ngram.items(), key=operator.itemgetter(1), reverse=True)
    return ngram

austen_sents    = gutenberg.sents('austen-emma.txt')
edgeworth_sents = gutenberg.sents('edgeworth-parents.txt')
melville_sents  = gutenberg.sents('melville-moby_dick.txt')

austen    = []
edgeworth = []
melville  = []

for j in austen_sents:
    austen.append(remove_bad_words(j))
for j in edgeworth_sents:
    edgeworth.append(remove_bad_words(j))
for j in melville_sents:
    melville.append(remove_bad_words(j))


print("----AUSTEN")

a_unigram = make_ngram(1, austen)
for i in range (0, 10):
    print(a_unigram[i])
print("----------")

a_bigram  = make_ngram(2, austen)
for i in range (0, 10):
    print(a_bigram[i])
print("----------")

a_trigram = make_ngram(3, austen)
for i in range (0, 10):
    print(a_trigram[i])
print("----------")


print("-EDGEWORTH")

e_unigram = make_ngram(1, edgeworth)
for i in range (0, 10):
    print(e_unigram[i])
print("----------")

e_bigram  = make_ngram(2, edgeworth)
for i in range (0, 10):
    print(e_bigram[i])
print("----------")

e_trigram = make_ngram(3, edgeworth)
for i in range (0, 10):
    print(e_trigram[i])
print("----------")


print("--MELVILLE")

m_unigram = make_ngram(1, melville)
for i in range (0, 10):
    print(m_unigram[i])
print("----------")

m_bigram  = make_ngram(2, melville)
for i in range (0, 10):
    print(m_bigram[i])
print("----------")

m_trigram = make_ngram(3, melville)
for i in range (0, 10):
    print(m_trigram[i])
print("----------")
