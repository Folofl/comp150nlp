# -*- coding: utf-8 -*-
# Assignment:  Final Project
# By:          Alena Borisenko 
#
# Submitted:   December 8th, 2017
#
# Description: This program gathers and saves tweets from
#              specified accounts via tweepy

import sys
import codecs
import textwrap
import tweepy
from   tweepy import OAuthHandler

if len(sys.argv) != 2:
    print("ERROR:    Not enough arguments. Please provide a username.")
    print("Example:  get_user_tweets.py @pamyurin")
    exit(1)

user = sys.argv[1]

print("Setting up tweepy...")

auth_info = {}
with open('auth_info.txt', 'r') as f:
    for line in f:
        splitLine = line.split()
        auth_info[splitLine[0]] = splitLine[1]

# Private auth info
consumer_key    = auth_info['consumer_key']
consumer_secret = auth_info['consumer_secret']
access_token    = auth_info['access_token']
access_secret   = auth_info['access_secret']

# Authorization
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
# Start tweepy
api = tweepy.API(auth)

# Specify where to hold them for now
tweets = []

# Request and save the user's 200 most recent tweets 
print("Finding tweets for user %s" % user)
recent_tweets = api.user_timeline(screen_name= user, count= 200)
# 200 seems to be the limit for a single search
# Could just be done here, but instead work around the 200 limit as shown here:
#     https://drive.google.com/file/d/0Bw1LIIbSl0xuNnJ0N1ppSkRjQjQ/view
while len(recent_tweets) > 0:
    tweets.extend(recent_tweets)
    oldest_id = recent_tweets[-1].id - 1
    recent_tweets = api.user_timeline(screen_name= user, count= 200, max_id=oldest_id)


# Create an .xml file and write info to it
file = codecs.open("xml/" + user + ".xml", 'wb', 'utf-8')
print("Writing to " + user +  ".xml...")
file.write("<tweets>")
tweet_num = 1
for status in tweets:
    # Used the following for object ref: 
    #     developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
    file.write("\n")
    file.write("    <tweet>\n")
    file.write("        <num>%d</num>\n"       % tweet_num)
    file.write("        <id_str>%s</id_str>\n" % status.id_str)
    file.write("        <user>%s</user>\n"     % status.user.screen_name)
    file.write("        <lang>%s</lang>\n"     % status.user.lang)
    file.write("        <text>\n")
    file.write(textwrap.indent(status.text, ' ' * 12))
    file.write("\n")
    file.write("        </text>\n")
    file.write("    </tweet>\n")
    tweet_num += 1
file.write("</tweets>")

print("Done!")
file.close()