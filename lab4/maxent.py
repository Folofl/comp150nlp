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

# gain access to XML data tags 
tree = ET.parse(train_file_name)
reviews = tree.getroot()

# gather ALL the possible words from reviews AND titles
all_words = []

for review in reviews:
    title       = review.find('title').text.strip().lower().split()
    review_text = review.find('review_text').text.strip().lower().split()
    all_words.extend(title)
    all_words.extend(review_text)

all_words = nltk.FreqDist(all_words)
all_words = all_words.most_common(2000)
word_features = list(i[0] for i in all_words)
print(word_features)



# features
# def review_features(review):
#     features = {}
#     for word in review:
#         features['contains({})'.format(word)] = word in re

# for review in reviews:
#     asin        = review.find('asin').text
#     print(asin)
#     rating      = review.find('rating').text.strip()
#     print(rating)
#     if float(rating) >= 4:
#         rating = 'Positive'
#     else:
#         rating = 'Negative'
#     helpful     = review.find('helpful').text.split()
#     if len(helpful) == 3:
#         helpful = int(helpful[0]) / int(helpful[2])
#     else:
#         helpful = -1
#     review_text = review.find('review_text').text
    
#     print(rating)
#     print(helpful)
#     print(review_text)
#     print('hallelujah' in review_text)


# features


# output:
# uniqueID $tab$ Positive/Negative