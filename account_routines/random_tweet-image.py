import tweepy
import random

##############
# connection #
##############

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

greetings = [
    "Greetings!",
    "Second Greeting.",
    "Third"
]

tags = [
    " #FirstTag",
    " #SecondTag",
    " #Et Cetera"
]
imageslist = [
    "IMG_1.JPG",
    "IMG_2.JPG",
    "IMG_3.JPG"
]

user = api.me()
print(user.name)

##################
# random message #
##################

def tweetRandomTweet():
    for i in range(100):
        m = random.choice(greetings)
        tagz1 = random.choice(tags)
        tagz2 = random.choice(tags)
        status = m + tagz1 + tagz2
        print(status)
        imagePath = random.choice(imageslist)
        print(imagePath)
        api.update_with_media(imagePath, status=status)
        print("got eem!")