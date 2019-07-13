import tweepy
from time import sleep
import random
import feedparser
import os

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

####################
# retweet from RSS #
####################

def ReadRssAndTweet():
    feed = feedparser.parse('https://www.google.com/alerts/feeds/04972117299862412355/8469625787646444303')
    for item in feed["items"]:
        title = item["title"]
        link = item["link"]
        # Make sure we don't post any duplicates.
        if not (IsUrlAlreadyPosted(link)):
            PostTweet(title, link)
            MarkUrlAsPosted(link)
            print("Posted: " + link)
        else:
            print("Already posted: " + link)

def IsTweetAlreadyRetweeted(tweetid):
    if os.path.isfile(Settings.PostedRetweetsOutputFile):
        # Check whether tweet IDs is in log file.
        f = open(Settings.PostedRetweetsOutputFile)
        posted_tweets = f.readlines()
        f.close()
        if (tweetid + "\n" or tweetid) in posted_tweets:
            return (True)
        else:
            return (False)
    else:
        return (False)