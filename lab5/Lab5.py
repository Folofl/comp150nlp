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


#Corpus: I like deep learning. I like NLP. I enjoy sailing.
la = np.linalg
words = ["I", "like", "enjoy", "deep", "learning", "NLP", "sailing", "."]

X = np.array([[0,2,1,0,0,0,0,0],
			  [2,0,0,1,0,1,0,0],
			  [1,0,0,0,0,0,1,0],
			  [0,1,0,0,1,0,0,0],
			  [0,0,0,1,0,0,0,1],
			  [0,1,0,0,0,0,0,1],
			  [0,0,1,0,0,0,0,1],
			  [0,0,0,0,1,1,1,0]])

U, s, V = la.svd(X, full_matrices=False)

for i in range(len(words)):
	plt.text(U[i, 0], U[i, 1], words[i])

plt.show()