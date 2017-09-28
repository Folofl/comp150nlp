# Assignment: Lab2
# By:         Alena Borisenko 
# Created:    September 25th, 2017
# Submitted:  September 27th, 2017

import operator
import nltk
import re
import numpy as np

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

from nltk.corpus import gutenberg
gutenberg.fileids()
['austen-emma.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt']

def remove_bad_words(target_list):
    bad_vals = [',', '.', ';', "'", '-', '!', '?', '"', ',"', ']', '!"', ';"', ',"--'
                '[', '(', ')', '."', '--', '.--', '!--', ';--', ',--', '?--', '?"']
    return [value for value in target_list if value not in bad_vals ] 

def make_ngram(n, source_sents):
    ngram = {}
    for sent in source_sents:
        for word_i in range(n - 1, len(sent)):
            context_key = ""
            if n == 1:
                context_key += "nocontext"
            else: 
                for k in range (word_i - (n - 1), word_i):
                    if k != (word_i - n + 1):
                        context_key += " "
                    context_key += sent[k]
            current_key = sent[word_i]
            if context_key in ngram:
                if current_key in ngram[context_key]:
                    ngram[context_key][current_key] += 1
                else:
                    ngram[context_key][current_key]  = 1
            else:
                ngram[context_key] = {}
                ngram[context_key][current_key]  = 1

    return ngram

def print_top_10(ngram):
    counter = 0;
    for i in ngram:
        if counter > 9:
            break
        print(i) 
        print(ngram[i])
        counter += 1

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


print("-------------a1-------------")

a1_unigram   = make_ngram(1, a1)
a1_bigram    = make_ngram(2, a1)
a1_trigram   = make_ngram(3, a1)
#a1_tetragram = make_ngram(4, a1)


print("-------------a2-------------")

a2_unigram   = make_ngram(1, a2)
a2_bigram    = make_ngram(2, a2)
a2_trigram   = make_ngram(3, a2)
#a2_tetragram = make_ngram(4, a2)


print("-------------a3-------------")

a3_unigram   = make_ngram(1, a3)
a3_bigram    = make_ngram(2, a3)
a3_trigram   = make_ngram(3, a3)
#a3_tetragram = make_ngram(4, a3)


print("-------a1 is choosing-------")

a1_sorted_unigram = {}

# Sort a1's unigram from most to least common
for i in a1_unigram:
    a1_sorted_unigram[i] = sorted(a1_unigram[i].items(), key=operator.itemgetter(1), reverse=True)

# get the top 100 most mentioned words
a1_top_words = []
for i in a1_sorted_unigram["nocontext"]:
    if len(a1_top_words) < 100:
        a1_top_words.append(i[0])
    else:
        break;

a2_points = 0
a3_points = 0
for i in a1_top_words:
    a1_candidates = sorted(a1_bigram[i].items(), key=operator.itemgetter(1), reverse=True)
    if i in a2_bigram:
        a2_candidates = sorted(a2_bigram[i].items(), key=operator.itemgetter(1), reverse=True)
    if i in a3_bigram:
        a3_candidates = sorted(a3_bigram[i].items(), key=operator.itemgetter(1), reverse=True)

    if a1_candidates[0][0] == a2_candidates[0][0]:
        a2_points +=  a2_candidates[0][1]
    if a1_candidates[0][0] == a3_candidates[0][0]:
        a3_points +=  a3_candidates[0][1]


print(a2_points, a3_points)
if   a2_points > a3_points:
    print("a2 wins")
elif a3_points > a2_points:
    print("a3 wins")
else:
    print("tie")

print("--------DIALOG START--------")

def generate_next_word (context, ngram):
    options       = []
    probabilities = []
    num_options   = 0
    if context in ngram:
        for candidate in ngram[context]:
            num_options += ngram[context][candidate]
        for candidate in ngram[context]:
            options.append(candidate)
            probabilities.append(ngram[context][candidate] / num_options)
        choice = np.random.choice(options, 1, p=probabilities)
        return choice[0]
    return "nocontext"

def generate_start_word (context, ngram, num_options):
    options       = []
    probabilities = []
    num_options   = a1_valid_word_count
    for candidate in a1_unigram[context]:
        options.append(candidate)
        probabilities.append(a1_unigram[context][candidate] / num_options)

    choice = np.random.choice(options, 1, p=probabilities)
    return choice[0]

def update_context (context_list):
    if len(context_list) == 0:
        return "nocontext"
    context = ""
    for i in context_list:
        if context == "":
            context += i
        else:
            context += " " + i
    return context

def generate_sentence (speaker, word_count, ngrams):
    context = "nocontext"
    context_list = []
    context = generate_start_word(context, ngrams[0], word_count)
    context_list.append(context)

    sentence = ""
    for i in range(0, 10):
        context_new = generate_next_word(context, ngrams[min(len(ngrams) - 1, len(context_list))])
        if context_new == "nocontext":
            context_list.pop(0)
            context = update_context(context_list)
        else:
            if sentence == "":
                sentence += context_new
            else:
                sentence += " " + context_new
            context_list.append(context_new)
            if len(context_list) > len(ngrams) - 1:
                context_list.pop(0)
                context = update_context(context_list)
            else:
                context += " " + context_new
    print(speaker + ": ", sentence)


generate_sentence ("A1", a1_valid_word_count, [a1_unigram, a1_bigram, a1_trigram])
generate_sentence ("A3", a3_valid_word_count, [a3_unigram, a3_bigram, a3_trigram])

generate_sentence ("A1", a1_valid_word_count, [a1_unigram, a1_bigram, a1_trigram])
generate_sentence ("A3", a3_valid_word_count, [a3_unigram, a3_bigram, a3_trigram])

print("---------DIALOG END---------")
print(" ")
print("-------a2 is choosing-------")

a2_sorted_unigram = {}

# Sort a2's unigram from most to least common
for i in a2_unigram:
    a2_sorted_unigram[i] = sorted(a2_unigram[i].items(), key=operator.itemgetter(1), reverse=True)

# get the top 100 most mentioned words
a2_top_words = []
for i in a2_sorted_unigram["nocontext"]:
    if len(a2_top_words) < 100:
        a2_top_words.append(i[0])
    else:
        break;

a1_points = 0
a3_points = 0
for i in a2_top_words:
    a2_candidates = sorted(a2_bigram[i].items(), key=operator.itemgetter(1), reverse=True)
    if i in a1_bigram:
        a1_candidates = sorted(a1_bigram[i].items(), key=operator.itemgetter(1), reverse=True)
    if i in a3_bigram:
        a3_candidates = sorted(a3_bigram[i].items(), key=operator.itemgetter(1), reverse=True)

    if a2_candidates[0][0] == a1_candidates[0][0]:
        a1_points +=  a1_candidates[0][1]
    if a2_candidates[0][0] == a3_candidates[0][0]:
        a3_points +=  a3_candidates[0][1]


print(a1_points, a3_points)
if   a1_points > a3_points:
    print("a1 wins")
elif a3_points > a1_points:
    print("a3 wins")
else:
    print("tie")

print("--------DIALOG START--------")
generate_sentence ("A2", a2_valid_word_count, [a2_unigram, a2_bigram, a2_trigram])
generate_sentence ("A3", a3_valid_word_count, [a3_unigram, a3_bigram, a3_trigram])

generate_sentence ("A2", a2_valid_word_count, [a2_unigram, a2_bigram, a2_trigram])
generate_sentence ("A3", a3_valid_word_count, [a3_unigram, a3_bigram, a3_trigram])

print("---------DIALOG END---------")