# Assignment: Lab5
# By:         Alena Borisenko 
# Created:    October 12th, 2017
# Submitted:  October 18th, 2017

import nltk
from   nltk.corpus   import brown
from   nltk.corpus   import stopwords
from   nltk.tokenize import RegexpTokenizer

import time
import re
import numpy as np
import matplotlib.pyplot as plt

from operator import itemgetter

# check if package is installed 
try:
    nltk.data.find('corpora/brown')
except LookupError:
    nltk.download('brown')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

np.set_printoptions(threshold=np.nan)
np.set_printoptions(suppress=True)

la = np.linalg

# corpus contains all words as they appear in brown corpus
#corpus = brown.raw()
corpus = brown.raw(categories='romance')
#corpus = "I think that is a cat, what about the dog's? Don't know"

corpus = corpus.lower()

# remove punctuation
tokenizer = RegexpTokenizer(r'\w+')
corpus = tokenizer.tokenize(corpus)

# remove stopwords
stopwords = set(stopwords.words('english'))
corpus = [word for word in corpus if word not in stopwords]

corp_len = len(corpus)

# words contains mapping: UNIQUE word key -> index in the X matrix
index = 0
words = {}
for i in corpus:
    if i not in words:
        words[i] = index;
        index += 1

sorted_words = sorted(words.items(), key=itemgetter(1))

dim = len(words)

#create a 2D array of size dim x dim; set all values to 0
X = np.zeros(shape=(dim, dim), dtype=int)

start = time.time()
win_size = 7
for i in range(0, corp_len):
    # check the left side
    left_i = i - 1
    countdown = win_size
    while (left_i >= 0) and (countdown > 0):
        X[ words[corpus[i]] ] [ words[corpus[left_i]] ] += 1
        left_i    -= 1
        countdown -= 1
    # check the right side
    right_i = i + 1
    countdown = win_size
    while (right_i < corp_len) and (countdown > 0):
        X[ words[corpus[i]] ] [ words[corpus[right_i]] ] += 1
        right_i   += 1
        countdown -= 1

print("Made X in %s seconds" % (time.time() - start))

# start = time.time()
# # save the matrix to a file for later use
# np.savetxt('matrix.txt', X, fmt='%i')
# print("---- %s seconds ---" % (time.time() - start))


#Corpus: I like deep learning. I like NLP. I enjoy sailing.
# la = np.linalg
# words = ["I", "like", "enjoy", "deep", "learning", "NLP", "sailing", "."]

# X2 = np.array([[0,2,1,0,0,0,0,0],
# 			     [2,0,0,1,0,1,0,0],
# 			     [1,0,0,0,0,0,1,0],
# 			     [0,1,0,0,1,0,0,0],
# 			     [0,0,0,1,0,0,0,1],
# 			     [0,1,0,0,0,0,0,1],
# 			     [0,0,1,0,0,0,0,1],
# 			     [0,0,0,0,1,1,1,0]])
# print(X2)

# U, s, V = la.svd(X, full_matrices=False)

# for i in range(len(words)):
# 	plt.text(U[i, 0], U[i, 1], words[i])

# plt.show()