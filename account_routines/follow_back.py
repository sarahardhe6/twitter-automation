import tweepy
from time import sleep
import random
import feedparser

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

#############################
# follow back all followers #
#############################
def followFollowers():
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        print("Followed everyone that is following " + user.name)
