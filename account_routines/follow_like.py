import tweepy
from time import sleep

consumer_key = '<CONSUMER_KEY>'
consumer_secret = '<CONSUMER_SECRET>'
access_token = '<ACCESS_TOKEN>'
access_token_secret = 'ACCESS_TOKEN_SECRET'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

api_count = 0
likes = 0
follows = 0

for tweet in tweepy.Cursor(api.search, q='topic to follow').items(200):
    try:
        tweet.favorite()
        print('\t' + "Liked")
        likes = likes + 1
        print(likes)
    except:
        #print(tweet)
        print('\tAlready Liked')
    if tweet.user.following:
        print("already following")
    else:
        try:
            tweet.user.follow()
            print('Followed the user')
            follows = follows + 1
            print(follows)
        except:
            print('Error: self-follow?')
    sleep(1)
