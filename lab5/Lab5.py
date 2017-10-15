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


la = np.linalg

# corpus contains all words as they appear in brown corpus
#corpus = brown.words()
#corpus = brown.words(categories='romance')
corpus = ["a", "b", "c", "a", "c", "d", "e", "a", "c", "d"]
corp_len = len(corpus)
print(corp_len)

# words contains mapping: UNIQUE word key -> index in the X matrix
index = 0
words = {}
for i in corpus:
    if i not in words:
        words[i] = index;
        index += 1

dim = len(words)
print(dim)

# create a 2D array of size dim x dim; set all values to 0
X = np.zeros(shape=(dim, dim))

# win_size = 2
# for i in range(0, corp_len):
#     if i < win_size:
        
#     elif i > (corp_len - win_size):
#     else:




# print(X)


#Corpus: I like deep learning. I like NLP. I enjoy sailing.
# la = np.linalg
# words = ["I", "like", "enjoy", "deep", "learning", "NLP", "sailing", "."]

# X2 = np.array([[0,2,1,0,0,0,0,0],
# 			  [2,0,0,1,0,1,0,0],
# 			  [1,0,0,0,0,0,1,0],
# 			  [0,1,0,0,1,0,0,0],
# 			  [0,0,0,1,0,0,0,1],
# 			  [0,1,0,0,0,0,0,1],
# 			  [0,0,1,0,0,0,0,1],
# 			  [0,0,0,0,1,1,1,0]])
# print(X2)

# U, s, V = la.svd(X, full_matrices=False)

# for i in range(len(words)):
# 	plt.text(U[i, 0], U[i, 1], words[i])

# plt.show()