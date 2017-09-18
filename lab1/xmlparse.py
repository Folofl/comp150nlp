# Assignment: Lab1
# By:         Alena Borisenko 
# Created:    September 18th, 2017
# Submitted:  September 20th, 2017

import re

source = open("Blithedale_Romance.txt", "r")
target = open("Blithedale_Romance.xml", "w")

data = source.read()

target.write("<book>\n")

chaptertitle = r"[I|V|X]+\. [A-Z '-]{2,}"

match = re.findall(chaptertitle, data)

if match:
    for x in match:
        target.write("<chaptertitle>")
        target.write("".join(x))
        target.write("</chaptertitle>\n")




target.write("\n</book>")

source.close()
target.close()
