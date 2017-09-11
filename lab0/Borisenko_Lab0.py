# Assignment: Lab0
# By:         Alena Borisenko 
# Created:    September  7th, 2017
# Submitted:  September 10th, 2017

import nltk
from nltk.corpus import gutenberg
gutenberg.fileids()
['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', ...]

# Step 1
file_flip = open("flip.txt", "r")
file_flop = open("flop.txt", "w")

flip_data = file_flip.read()


# Step 2
# file_flop.write(flip_data + "\n")


# Step 3
for i in range (0, len(flip_data)):
    file_flop.write(flip_data[len(flip_data) - 1 - i])

file_flop.write("\n")

flop_data = flip_data.split()
flop_data.reverse()
file_flop.write(" ".join(flop_data))

file_flop.write("\n")


# Step 4
emma = gutenberg.words('austen-emma.txt')
file_flop.write(str(len(emma)))
file_flop.write("\n")


# Step 5
# Think about final project


# Step 6
# Experissions in which literal meaning doesn't match intended meaning
file_flop.write("My head is killing me\n")
file_flop.write("She broke his heart")


# Close files
file_flip.close()
file_flop.close()