# Assignment: Lab1
# By:         Alena Borisenko 
# Created:    September 18th, 2017
# Submitted:  September 20th, 2017

source = open("Blithedale_Romance.txt", "r")
target = open("Blithedale_Romance.xml", "w")


target.write("<book>\n")
target.write("\n</book>")

source.close()
target.close()
