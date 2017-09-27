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

a_unigram = {}
a_bigram  = {}
a_trigram = {}

e_unigram = {}
e_bigram  = {}

m_unigram = {}
m_bigram  = {}


print("----AUSTEN")
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
print(a_unigram[3])
print(a_unigram[4])
print(a_unigram[5])
print(a_unigram[6])
print(a_unigram[7])
print(a_unigram[8])
print(a_unigram[9])
print("----------")

for j in austen:
    for i in range(1, len(j)):
        two_words  = j[i - 1] + " " + j[i]
        if two_words in a_bigram:
            a_bigram[two_words] += 1
        else:
            a_bigram[two_words] = 1

a_bigram = sorted(a_bigram.items(), key=operator.itemgetter(1), reverse=True)

print(a_bigram[0])
print(a_bigram[1])
print(a_bigram[2])
print(a_bigram[3])
print(a_bigram[4])
print(a_bigram[5])
print(a_bigram[6])
print(a_bigram[7])
print(a_bigram[8])
print(a_bigram[9])
print("----------")

for j in austen:
    for i in range(2, len(j)):
        three_words  = j[i - 2] + " " + j[i - 1] + " " + j[i]
        if three_words in a_trigram:
            a_trigram[three_words] += 1
        else:
            a_trigram[three_words] = 1

a_trigram = sorted(a_trigram.items(), key=operator.itemgetter(1), reverse=True)

print(a_trigram[0])
print(a_trigram[1])
print(a_trigram[2])
print(a_trigram[3])
print(a_trigram[4])
print(a_trigram[5])
print(a_trigram[6])
print(a_trigram[7])
print(a_trigram[8])
print(a_trigram[9])
print("----------")

# print("-EDGEWORTH")
# # go through every word
# for j in edgeworth:
#     for i in j:
#         if i in e_unigram:
#             e_unigram[i] += 1
#         else:
#             e_unigram[i] = 1

# e_unigram = sorted(e_unigram.items(), key=operator.itemgetter(1), reverse=True)

# # print(e_unigram[0])
# # print(e_unigram[1])
# # print(e_unigram[2])
# # print(e_unigram[3])
# # print(e_unigram[4])
# # print(e_unigram[5])
# # print(e_unigram[6])
# # print(e_unigram[7])
# # print(e_unigram[8])
# # print(e_unigram[9])
# # print("----------")

# for j in edgeworth:
#     for i in range(1, len(j)):
#         two_words = j[i - 1] + " " + j[i]
#         if two_words in e_bigram:
#             e_bigram[two_words] += 1
#         else:
#             e_bigram[two_words] = 1

# e_bigram = sorted(e_bigram.items(), key=operator.itemgetter(1), reverse=True)

# # print(e_bigram[0])
# # print(e_bigram[1])
# # print(e_bigram[2])
# # print(e_bigram[3])
# # print(e_bigram[4])
# # print(e_bigram[5])
# # print(e_bigram[6])
# # print(e_bigram[7])
# # print(e_bigram[8])
# # print(e_bigram[9])
# # print("----------")

# print("--MELVILLE")
# # go through every word
# for j in melville:
#     for i in j:
#         if i in m_unigram:
#             m_unigram[i] += 1
#         else:
#             m_unigram[i] = 1

# m_unigram = sorted(m_unigram.items(), key=operator.itemgetter(1), reverse=True)

# # print(m_unigram[0])
# # print(m_unigram[1])
# # print(m_unigram[2])
# # print(m_unigram[3])
# # print(m_unigram[4])
# # print(m_unigram[5])
# # print(m_unigram[6])
# # print(m_unigram[7])
# # print(m_unigram[8])
# # print(m_unigram[9])
# # print("----------")

# for j in melville:
#     for i in range(1, len(j)):
#         two_words = j[i - 1] + " " + j[i]
#         if two_words in m_bigram:
#             m_bigram[two_words] += 1
#         else:
#             m_bigram[two_words] = 1

# m_bigram = sorted(m_bigram.items(), key=operator.itemgetter(1), reverse=True)

# # print(m_bigram[0])
# # print(m_bigram[1])
# # print(m_bigram[2])
# # print(m_bigram[3])
# # print(m_bigram[4])
# # print(m_bigram[5])
# # print(m_bigram[6])
# # print(m_bigram[7])
# # print(m_bigram[8])
# # print(m_bigram[9])
# # print("----------")

# target.close()