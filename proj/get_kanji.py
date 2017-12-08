# -*- coding: utf-8 -*-
# Assignment:  Final Project
# By:          Alena Borisenko 
#
# Submitted:   December 8th, 2017
#
# Description: This program extracts the kanji from a .csv study guide
#              Kanji source: http://tangorin.com/common_kanji

import csv

def extract_kanji(source_filename, target_filename):
    # Open and read from the source file
    with open(source_filename, 'r') as source_file:
        # Start reading the source file
        reader = csv.reader(source_file, delimiter='\t')

        # Large string to hold the characters
        kanji_list = ""
        for row in reader:
            # Add a space in front if it's not the first character
            if (kanji_list != ""):
                kanji_list += " "
            kanji_list += row[0]

        # Open and write to the target file
        with open(target_filename, "w") as target_file:
            target_file.write(kanji_list)

        # Notify user that a file has been written
        print("Wrote %s" % target_filename)
    return

# For each JLPT level (1 to 5)
for lvl in range(1, 6):
    source_filename = "kanji/csv/tangorin_2000" + str(lvl) + ".csv"
    target_filename = "kanji/txt/jlpt_n"        + str(lvl) + ".txt"

    extract_kanji(source_filename, target_filename)

# For each Jōyō grade (1 to 7)
for lvl in range(1, 8):
    source_filename = "kanji/csv/tangorin_100" + str(lvl) + ".csv"
    target_filename = "kanji/txt/jōyō_g"       + str(lvl) + ".txt"

    extract_kanji(source_filename, target_filename)

print("Done!")
