# Assignment: Lab1
# By:         Alena Borisenko 
# Created:    September 18th, 2017
# Submitted:  September 20th, 2017

import re

source = open("Blithedale_Romance.txt", "r")
target = open("Blithedale_Romance.xml", "w")

data = source.read()

target.write("<book>\n")

# This assumes future books follow the same title/author format
# Alternatively could read the first few lines
b_info = r"[A-Z].*\n\nby\n\n[A-Z].*"

# Assumes chapter names are labeled using Roman numerals
ch_title  = r"[I|V|X]+\. [A-Z '-]{2,}"

b_info_match   = re.search(b_info, data)
ch_title_match = re.findall(ch_title, data)

if b_info_match:
    b_info_match = b_info_match[0].split('\n\n')
    target.write("<booktitle>")
    target.write(b_info_match[0])
    target.write("</booktitle>\n")
    target.write("<author>")
    target.write(b_info_match[2])
    target.write("</author>\n")

if ch_title_match:
    for x in ch_title_match:
        target.write("<chapter>\n")
        target.write("<chaptertitle>")
        target.write("".join(x))
        target.write("</chaptertitle>\n")
        target.write("</chapter>\n")




target.write("\n</book>")

source.close()
target.close()
