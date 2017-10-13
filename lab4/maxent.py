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
import re
import xml.etree.ElementTree as ET

# read in command line arguments specifying filenames
train_file_name = sys.argv[-2]
test_file_name  = sys.argv[-1]

# gain access to XML data tags 
train_tree    = ET.parse(train_file_name)
train_reviews = train_tree.getroot()

test_tree     = ET.parse(test_file_name)
test_reviews  = test_tree.getroot()

# gather ALL the possible words from train_reviews, include titles
all_words = []

for review in train_reviews:
    title       = review.find('title').text.strip().lower()
    title       = re.sub(r'[^\w\s]', '', title).split()
    review_text = review.find('review_text').text.strip().lower()
    review_text = re.sub(r'[^\w\s]', '', review_text).split()
    all_words.extend(title)
    all_words.extend(review_text)

all_asin    = []
#all_ratings = []

for review in test_reviews:
    asin = review.find('asin').text.strip()
    # rating      = review.find('rating').text.strip()
    # if float(rating) >= 4:
    #     rating = 'pos'
    # else:
    #     rating = 'neg'
    all_asin.append(asin)
    #all_ratings.append(rating)

# get the X most common words featured in train_reviews/their titles
# higher X => slower but more accurate, as show by testing on train_set:
#      num words     % correct        time
#         ALL           ~95         ~10 min
#        5000           ~87         ~45 sec
#        3000           ~83         ~25 sec
#        2000           ~79         ~16 sec
all_words = nltk.FreqDist(all_words)
all_words = all_words.most_common(5000)
word_features = list(i[0] for i in all_words)

# check if a given review contains the words we look for
def review_features(review):
    review_text = review.find('review_text').text.strip().lower()
    review_text = re.sub(r'[^\w\s]', '', review_text).split()
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in review_text)
    return features

test_review = train_reviews.find('review')

# train classifier
train_set = []
for review in train_reviews:
    rating      = review.find('rating').text.strip()
    if float(rating) >= 4:
        rating = 'pos'
    else:
        rating = 'neg'
    train_set.append((review_features(review), rating))

test_set = []
for review in test_reviews:
    test_set.append((review_features(review)))

#print(train_set)

classifier = nltk.NaiveBayesClassifier.train(train_set)
classifier.show_most_informative_features(100)
predictions = classifier.classify_many(test_set)

for i in range(0, len(predictions)):
    print(all_asin[i], "\t", ("Positive" if predictions[i] == "pos" else "Negative"))
