# Assignment: Lab4
# By:         Alena Borisenko 
# Submitted:  October 13th, 2017
#
# Note:       Using Noah Cooper's updated xml file

import nltk
import sys

# read in command line arguments specifying filenames
train_file_name = sys.argv[-2]
test_file_name  = sys.argv[-1] 

# output:
# uniqueID $tab$ Positive/Negative