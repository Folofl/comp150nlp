# Assignment:  Final Project
# By:          Alena Borisenko 
#
# Submitted:   December 8th, 2017
#
# Description: 

import nltk
import sys
import re
import operator
import xml.etree.ElementTree as ET
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def webapp():
    if   request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        username = request.form['username']
        # Gain access to XML data tags 
        tweet_tree    = ET.parse("xml/" + username + ".xml")
        tweets        = tweet_tree.getroot()

        # All kanji from tweets will be stored/counted in this dictionary 
        kanji_dict  = {}

        # Many attempts later I found that somebody has already figured it out:
        #     https://gist.github.com/terrancesnyder/1345094
        kanji_regex = re.compile('[一-龯]')

        # Read in the tweet data
        for tweet in tweets:
            tweet_text  = tweet.find('text').text.strip()
            tweet_kanji = [c for c in tweet_text if kanji_regex.match(c)]
            for kanji in tweet_kanji:
                if kanji in kanji_dict:
                    kanji_dict[kanji] += 1
                else:
                    kanji_dict[kanji] = 1

        # Uncomment to print out top 100 most common kanji
        top_kanji = sorted(kanji_dict.items(), key=operator.itemgetter(1), reverse=True)
        top_kanji = top_kanji[:20]
        # for i in range(0, 100):
        #    print(top_kanji[i])

        #                 N/A  N1  N2  N3  N4  N5
        num_jlpt_kanji = [  0,  0,  0,  0,  0,  0]
        jlpt_kanji = {}
        for lvl in range(5, 0, -1):
            with open("kanji/txt/jlpt_n" + str(lvl) + ".txt", 'r') as f:
                for line in f:
                    kanji_list = line.split()
                    for kanji in kanji_list:
                        jlpt_kanji[kanji] = lvl
                        num_jlpt_kanji[lvl] += 1

        #                 N/A  G1  G2  G3  G4  G5  G6  G7
        num_joyo_kanji = [  0,  0,  0,  0,  0,  0,  0,  0]
        joyo_kanji = {}
        for grade in range(7, 0, -1):
            with open("kanji/txt/jōyō_g" + str(grade) + ".txt", 'r') as f:
                for line in f:
                    kanji_list = line.split()
                    for kanji in kanji_list:
                        joyo_kanji[kanji] = grade
                        num_joyo_kanji[grade] += 1


        print("Total number of unique kanji in tweets: %d" % len(kanji_dict))
        print("Total number of        kanji in JLPT:   %d" % len(jlpt_kanji))
        print("Total number of        kanji in Jōyō:   %d" % len(joyo_kanji))

        #                 N/A  N1  N2  N3  N4  N5
        jlpt_kanji_use = [  0,  0,  0,  0,  0,  0]
        #                 N/A  G1  G2  G3  G4  G5  G6  G7
        joyo_kanji_use = [  0,  0,  0,  0,  0,  0,  0,  0]
        mystery_kanji  = []
        for kanji in kanji_dict:
            if kanji in jlpt_kanji:
                jlpt_kanji_use[jlpt_kanji[kanji]] += 1
            else:
                jlpt_kanji_use[0] += 1

            if kanji in joyo_kanji:
                joyo_kanji_use[joyo_kanji[kanji]] += 1
            else:
                joyo_kanji_use[0] += 1

            if kanji not in jlpt_kanji and kanji not in joyo_kanji:
                mystery_kanji.append(kanji)

        print("Percent of JLPT kanji used:")
        print("    N5: %f" % ((jlpt_kanji_use[5] / num_jlpt_kanji[5])*100))
        print("    N4: %f" % ((jlpt_kanji_use[4] / num_jlpt_kanji[4])*100))
        print("    N3: %f" % ((jlpt_kanji_use[3] / num_jlpt_kanji[3])*100))
        print("    N2: %f" % ((jlpt_kanji_use[2] / num_jlpt_kanji[2])*100))
        print("    N1: %f" % ((jlpt_kanji_use[1] / num_jlpt_kanji[1])*100))
        print("Percent of Jōyō kanji used:")
        print("    G1: %f" % ((joyo_kanji_use[1] / num_joyo_kanji[1])*100))
        print("    G2: %f" % ((joyo_kanji_use[2] / num_joyo_kanji[2])*100))
        print("    G3: %f" % ((joyo_kanji_use[3] / num_joyo_kanji[3])*100))
        print("    G4: %f" % ((joyo_kanji_use[4] / num_joyo_kanji[4])*100))
        print("    G5: %f" % ((joyo_kanji_use[5] / num_joyo_kanji[5])*100))
        print("    G6: %f" % ((joyo_kanji_use[6] / num_joyo_kanji[6])*100))
        print("    G7: %f" % ((joyo_kanji_use[7] / num_joyo_kanji[7])*100))
        print("Number of unique kanji not part of JLPT or Jōyō:")
        print("    %d out of %d" % (len(mystery_kanji), len(kanji_dict)))

        return render_template("result.html", 
                               user=username, 
                               jlpt_kanji_use=jlpt_kanji_use, 
                               joyo_kanji_use=joyo_kanji_use, 
                               num_jlpt_kanji=num_jlpt_kanji, 
                               num_joyo_kanji=num_joyo_kanji,
                               top_kanji=top_kanji)

if __name__ == "__main__":
    app.run()
