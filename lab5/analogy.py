# Assignment:  Lab5
# By:          Alena Borisenko 
# Created:     October 17th, 2017
# Submitted:   October 18th, 2017
#
# Description: Once generate_matromatrix.py has been generated the
#              required matrices and keys/words, this program will
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
X  = np.load('Xmatrix.npy')

# # load the U matrix
# U  = np.load('Umatrix.npy')

# load the kU matrix
kU = np.load('kUmatrix.npy')


def check_input(A, B, C):
    D = "OK"

    if A not in keys:
        print("ERROR: {} is not in the term list".format(A))
        D = "ERROR"
    if B not in keys:
        print("ERROR: {} is not in the term list".format(B))
        D = "ERROR"
    if C not in keys:
        print("ERROR: {} is not in the term list".format(C))
        D = "ERROR"

    return D

def find_analogy(matrix, user_input, A, B, C):
    input_status = check_input(A, B, C)
    if input_status == "ERROR":
        return 

    # need to compare results of the following equation:
    #     || D - C + A - B ||^2  
    # =>  || D + A - B - C ||^2  
    # =>  || A - B - C + D ||^2

    # A - B
    ABdiff  = np.subtract(matrix[ words[A] ], matrix[ words[B] ])
    # A - B - C
    ABCdiff = np.subtract(ABdiff, matrix[ words[C] ])

    D = "UNKNOWN"
    curr_min = 10000000
    for key in keys:
        if key != A and key != B and key != C:
            #    A - B - C + D
            ABCD    = np.add(ABCdiff, matrix[ words[key] ])
            # || A - B - C + D ||
            ABCDmag = np.linalg.norm(ABCD)
            # || A - B - C + D ||^2
            result  = np.power(ABCDmag, 2)

            if result < curr_min:
                curr_min = result
                D = key

    if (D != "UNKNOWN"):
            print(user_input, D)

user_input= ""

while (True):
    user_input = input("Please enter an analogy\n")

    if user_input == "quit":
        break

    input_list = user_input.split()

    # check the format
    if (len(input_list)   != 8    or 
            input_list[1] != "is" or 
            input_list[2] != "to" or
            input_list[4] != "as" or
            input_list[6] != "is" or
            input_list[7] != "to"):
        print("Expected format: A is to B as C is to \n")
    else:
        print("Please wait...")
        A  = input_list[0]
        B  = input_list[3]
        C  = input_list[5]
        find_analogy( X, user_input, A, B, C)
        #find_analogy( U, user_input, A, B, C)
        find_analogy(kU, user_input, A, B, C)
        print("")