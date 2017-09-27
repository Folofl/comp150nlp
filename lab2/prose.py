# Assignment: Lab2
# By:         Alena Borisenko 
# Created:    September 25th, 2017
# Submitted:  September 26th, 2017

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
    bad_vals = [',', '.', ';', "'", '-', '!', '?', '"', ',"', ']', 
                '[', '(', ')', '."', '--', '.--', '!--', ';--']
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
#sorted_ngram = {}
    #for i in ngram:
    #    sorted_ngram[i] = sorted(ngram[i].items(), key=operator.itemgetter(1), reverse=True)
    #return sorted_ngram



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

def generate_sentence (word_count, ngrams):
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
    print(sentence)


generate_sentence (a1_valid_word_count, [a1_unigram, a1_bigram, a1_trigram])
generate_sentence (a2_valid_word_count, [a2_unigram, a2_bigram, a2_trigram])
generate_sentence (a3_valid_word_count, [a3_unigram, a3_bigram, a3_trigram])

