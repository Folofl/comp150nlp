# Assignment: Lab4
# By:         Alena Borisenko 
# Submitted:  October 13th, 2017
#
# Note:       Using Noah Cooper's updated xml file
#             Not sure about MacOS, but Windows gives a unicode
#             error unless you run the following in the console:
#                 chcp 65001

import nltk
import sys
import xml.etree.ElementTree as ET

# read in command line arguments specifying filenames
train_file_name = sys.argv[-2]
test_file_name  = sys.argv[-1]

tree = ET.parse(train_file_name)
reviews = tree.getroot()

for review in reviews:
    asin        = review.find('asin').text
    rating      = review.find('rating').text
    helpful     = review.find('helpful').text
    review_text = review.find('review_text').text
    print(asin)
    print(rating)
    print(helpful)
    print(review_text)

# features


# output:
# uniqueID $tab$ Positive/Negative