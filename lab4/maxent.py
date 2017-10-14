# Assignment: Lab4
# By:         Alena Borisenko 
# Submitted:  October 13th, 2017
#
# Note:       Using Noah Cooper's updated xml file
#             Not sure about MacOS, but Windows gives a unicode
#             error unless you run the following in the console:
#                 chcp 65001
#             Accuracy and execution time depend on the number of
#             words analyzed, currently set to 5000 for a more
#             managable run time. See below for more info. 

import nltk
import sys
import re
import xml.etree.ElementTree as ET

# read in command line arguments specifying filenames
train_file_name = sys.argv[-2]
test_file_name  = sys.argv[-1]

# gain access to XML data tags 
train_tree    = ET.parse(train_file_name)
test_tree     = ET.parse(test_file_name)
train_reviews = train_tree.getroot()
test_reviews  = test_tree.getroot()

# gather ALL the possible words from train_reviews, include titles
all_words = []
for review in train_reviews:
    # extract text, lowercase it, remove punctuation, separate into list
    title       = review.find('title').text.strip().lower()
    title       = re.sub(r'[^\w\s]', '', title).split()
    review_text = review.find('review_text').text.strip().lower()
    review_text = re.sub(r'[^\w\s]', '', review_text).split()
    all_words.extend(title)
    all_words.extend(review_text)

# gether ALL the unique ids for the output
all_asin    = []
for review in test_reviews:
    asin = review.find('asin').text.strip()
    all_asin.append(asin)

# get the X most common words featured in train_reviews/their titles
# higher X => slower but more accurate, as show by testing on full train set
#      num words     % correct        time
#        7000           ~93         ~ 1 min 53 sec
#        5000           ~90         ~ 1 min 20 sec
#        3000           ~87         ~       55 sec
#        2000           ~84         ~       30 sec
all_words = nltk.FreqDist(all_words)
all_words = all_words.most_common(5000)
word_features = list(i[0] for i in all_words)

# check if a given review contains the words we look for
def review_features(review):
    title       = review.find('title').text.strip().lower()
    title       = re.sub(r'[^\w\s]', '', title).split()
    review_text = review.find('review_text').text.strip().lower()
    review_text = re.sub(r'[^\w\s]', '', review_text).split()

    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in review_text or word in title)

    # optional feature: consider helpfulness
    # this barely improves results, guess negative reviews can be helpful too :c
    # helpful     = review.find('helpful').text.split()
    # if len(helpful) == 3:
    #     help_rating = int(helpful[0]) / int(helpful[2])
    #     if help_rating >= 0.6:
    #         features['helpful rating'] = True
    #     else:
    #         features['helpful rating'] = False

    return features

# prepare the training set (knows correct ratings)
train_set = []
for review in train_reviews:
    rating      = review.find('rating').text.strip()
    # convert from raw rating value to pos/neg string
    if float(rating) >= 4:
        rating = 'pos'
    else:
        rating = 'neg'
    # append the list-rating tuple
    train_set.append((review_features(review), rating))

# prepare the test set (does not know rating info)
test_set = []
for review in test_reviews:
    test_set.append((review_features(review)))

# train the classifier
classifier = nltk.NaiveBayesClassifier.train(train_set)
# generate predictions for the test set
predictions = classifier.classify_many(test_set)

# print out each prediction side by side with its unique id
for i in range(0, len(predictions)):
    print(all_asin[i], "\t", ("Positive" if predictions[i] == "pos" else "Negative"))