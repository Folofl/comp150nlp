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
    keys  = pickle.load(fp)
# unpickle matrix word dict
with open ('words', 'rb') as fp:
    words = pickle.load(fp)
    
# load the X matrix
X = np.load('Xmatrix.npy')
# load the U matrix
U = np.load('Umatrix.npy')

def find_analogy(A, B, C):
    D = "UNKNOWN"
    if A not in keys:
        print("ERROR: {} is not in the term list".format(A))
        D = "ERROR"
    if B not in keys:
        print("ERROR: {} is not in the term list".format(B))
        D = "ERROR"
    if C not in keys:
        print("ERROR: {} is not in the term list".format(C))
        D = "ERROR"

    if D == "ERROR":
        return D

    print(words[A])
    print(words[B])
    print(words[C])

    return D

user_input= ""

while (True):
    user_input = input("Please enter an analogy\n")

    if user_input == "quit":
        break

    input_list = user_input.split()

    if (len(input_list)   != 8    or 
            input_list[1] != "is" or 
            input_list[2] != "to" or
            input_list[4] != "as" or
            input_list[6] != "is" or
            input_list[7] != "to"):
        print("Expected format: A is to B as C is to \n")
    else:
        print("Please wait...")
        A = input_list[0]
        B = input_list[3]
        C = input_list[5]
        D = find_analogy(A, B, C)
        if (D != "ERROR"):
            print(user_input, D, "\n")