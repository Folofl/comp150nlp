# Assignment:  Lab5
# By:          Alena Borisenko 
# Created:     October 12th, 2017
# Submitted:   October 18th, 2017
#
# Description: Once a matrix has been generated, this program will
#              (attempt to) complete user-requested analogies.

import pickle
import numpy as np

# unpickle matrix terms
with open ('keys', 'rb') as fp:
    keys = pickle.load(fp)

# load the X matrix
X = np.load('Xmatrix.npy')
# load the U matrix
U = np.load('Umatrix.npy')

user_input= ""

while (True):
    user_input = input("Please enter an analogy\n")

    if user_input == "quit":
        break

    user_input = user_input.split()

    if (len(user_input)   != 8    or 
            user_input[1] != "is" or 
            user_input[2] != "to" or
            user_input[4] != "as" or
            user_input[6] != "is" or
            user_input[7] != "to"):
        print("Expected format: X is to Y as Z is to\n")
    else:
        print("Please wait...\n")