# Assignment: Lab1
# By:         Alena Borisenko 
# Created:    September 18th, 2017
# Submitted:  September 20th, 2017

import re

################################################################
# RegEx used 
################################################################
# Book Info Template.     (Assumed based on book format)
b_info    = r"[A-Z].*\n\nby\n\n[A-Z].*"
# Chapter Title Template. (Assumed to use Roman numerals)
ch_title  = r"[I|V|X]+\. [A-Z '-]{2,}"
# Proper Noun Template.   (Allows multiple words and honorifics)
prop_nouns = r"(?<=\, |[a-z] |[a-z]\n)(?:(?:Mrs\.|Mr\.|Miss|Dr\.) *)?(?:[A-Z][a-z]+(?: *[A-Z][a-z]+)*)+"
# Capitalized words to be ignored later.
months   = r"(?:January|February|March|April|\bMay\b|June|July|August|September|October|November|December)[s ]*"
days     = r"(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)[s ]*"
pronouns = r"(?:\bHe\b|\bHim\b|\bHis\b|\bShe\b|\bHer\b|\bMy\b)"
################################################################


# Get the source and target files ready
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


# Open the book tag
target.write("<book>\n")

# Look for author and title info
b_info_match   = re.search(b_info, data)
# Write to file if found
if b_info_match:
    b_info_match = b_info_match.group(0)
    b_info_match = b_info_match.split('\n\n')
    target.write("<booktitle>")
    target.write(b_info_match[0])
    target.write("</booktitle>\n")
    target.write("<author>")
    target.write(b_info_match[2])
    target.write("</author>\n")

# Look for all capitalized nouns
p_nouns = re.findall(prop_nouns, data)
p_nouns = set(p_nouns)
# Write to file if found
if p_nouns:
    target.write("<propernouns>\n")
    for n in p_nouns:
        # Remove the boring ones
        n = re.sub(months,   '', n)
        n = re.sub(days,     '', n)
        n = re.sub(pronouns, '', n)
        if n != "":
            n = re.sub('\n', ' ', n)
            target.write(n)
            target.write(", ")
    target.write("\n</propernouns>")


# Split the data into paragraphs
paragraphs = re.split(r"\n\n", data)

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

# Close files
source.close()
target.close()
