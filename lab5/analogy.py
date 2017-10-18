# Assignment:  Lab5
# By:          Alena Borisenko 
# Created:     October 12th, 2017
# Submitted:   October 18th, 2017
#
# Description: Once a matrix has been generated, this program will
#              (attempt to) complete user-requested analogies.

user_input= ""

while (True):
    user_input = input("Please enter an analogy\n")
    if user_input == "quit":
        break
        
    print(user_input)
    print("Please wait...\n")