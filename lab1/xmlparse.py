# Assignment: Lab1
# By:         Alena Borisenko 
# Created:    September 18th, 2017
# Submitted:  September 20th, 2017

import re

source = open("Blithedale_Romance.txt", "r")
target = open("Blithedale_Romance.xml", "w")

# Read in the original book 
data = source.read()

# While data is "whole", replace all quotation marks
# Note that this can't tell the diff between quotes and "air quotes"
data = re.sub('\"\n', '</quote>\n', data)
data = re.sub('\" ', '</quote> ', data)
data = re.sub('\n\"', '\n<quote>', data)
data = re.sub(' \"', ' <quote>', data)

# Above substitutions separated into space/newline cases to preserve formatting
# A better regex for finding quotes would be: 
    # Finds things in quotation marks
    # quote     = r"\"[^\"]+\""
    # Finds things in quotation marks, but returns only the content
    # quoteless = r"(?<=\")[^ \n][^\"]+[^ ](?=\")"

# Split the data into paragraphs
paragraphs = re.split(r"\n\n", data)

# Assumes future books follow the same title/author format
b_info    = r"[A-Z].*\n\nby\n\n[A-Z].*"

# Assumes chapter names are labeled using Roman numerals
ch_title  = r"[I|V|X]+\. [A-Z '-]{2,}"

# Open the book tag
target.write("<book>\n")

# Look for author and title info
b_info_match   = re.search(b_info, data)
# Write to file if found
if b_info_match:
    b_info_match = b_info_match[0].split('\n\n')
    target.write("<booktitle>")
    target.write(b_info_match[0])
    target.write("</booktitle>\n")
    target.write("<author>")
    target.write(b_info_match[2])
    target.write("</author>\n")

# Handle chapters and paragraphs next
# Note that titles are "exceptions" and get <chaptertitle> not <paragraph> tag
for x in paragraphs[3:]:
    title  = re.findall(ch_title, x)
    
    # Check if this is a title
    if title:
        # Format the title
        for y in title:
            # Print closing chapter tag if this is not the first chapter
            if y[0]+y[1] != 'I.':
                target.write("</chapter>\n")
            target.write("\n<chapter>\n")
            target.write("<chaptertitle>")
            target.write("".join(y))
            target.write("</chaptertitle>\n")
    # Ignore the empty string caused by extra \n between chapters
    elif x == "":
        target.write(x)
    # Format paragraphs
    else:
        target.write("<paragraph>\n")
        target.write(x)
        target.write("\n</paragraph>\n")

# Closing tags
target.write("</chapter>")
target.write("\n</book>")

source.close()
target.close()
