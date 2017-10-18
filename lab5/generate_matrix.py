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
import pickle
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

# corpus contains all words with repetitions
# corpus = brown.raw() # does not play nice with SVD bc of the size
corpus = brown.raw(categories='romance')

# make everything lowercase
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
keys  = []
for i in corpus:
    if i not in words:
        words[i] = index;
        keys.append(i)
        index += 1
term = len(words)
# save keys for use by analogy.py
with open('keys', 'wb') as fp:
    pickle.dump(keys, fp)
# save words for use by analogy.py
with open('words', 'wb') as fp:
    pickle.dump(words, fp)

#create a 2D array of size term x term; set all values to 0
X = np.zeros(shape=(term, term), dtype=int)

start = time.time()

# look for matching words in a window of _ words to the left/right
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

start = time.time()
# compute the SVD decomposition of the matrix
#   U = matrix containing the left  singular vectors of X
#   s = vector containing the       singular values  of X
#   V = matrix containing the right singular vectors of X
U, s, V = la.svd(X, full_matrices=False, compute_uv=True)
print("Made U in %s seconds" % (time.time() - start))

start = time.time()
np.save('Xmatrix.npy', X)
print("Saved  Xmatrix.npy in %s seconds" % (time.time() - start))

start = time.time()
np.save('Umatrix.npy', U)
print("Saved  Umatrix.npy in %s seconds" % (time.time() - start))