# Assignment: Lab5
# By:         Alena Borisenko 
# Created:    October 12th, 2017
# Submitted:  October 18th, 2017

import nltk
from nltk.corpus import brown

import numpy as np
import matplotlib.pyplot as plt

# check if package is installed 
try:
    nltk.data.find('corpora/brown')
except LookupError:
    nltk.download('brown')

np.set_printoptions(threshold=np.nan)
np.set_printoptions(suppress=True)

la = np.linalg

# corpus contains all words as they appear in brown corpus
#corpus = brown.words()
#corpus = brown.words(categories='romance')
#corpus = ["I", "like", "deep", "learning", ".", "I", "like", "NLP", ".", "I", "enjoy", "sailing", "."]
corpus = ["a", "b", "c", "a", "c", "d", "e", "a", "c", "d"]
corp_len = len(corpus)

# words contains mapping: UNIQUE word key -> index in the X matrix
index = 0
words   = {}
indices = {}
for i in corpus:
    if i not in words:
        words[i] = index;
        index += 1
print(words)

# words = {"I":0, "like":1, "enjoy":2, "deep":3, "learning":4, "NLP":5, "sailing":6, ".":7}
dim = len(words)

# create a 2D array of size dim x dim; set all values to 0
X = np.zeros(shape=(dim, dim), dtype=int)

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

# save the matrix to a file for later use
#np.savetxt('matrix.txt', X, fmt='%i')



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