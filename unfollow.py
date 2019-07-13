import time
import tweepy

############
# account1 #
############

# consumer_key = '<CONSUMER_KEY>'
# consumer_secret = '<CONSUMER_SECRET>'
# access_token = '<ACCESS_TOKEN>'
# access_token_secret = 'ACCESS_TOKEN_SECRET''
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

############
# account2 #
############

# consumer_key = '<CONSUMER_KEY>'
# consumer_secret = '<CONSUMER_SECRET>'
# access_token = '<ACCESS_TOKEN>'
# access_token_secret = 'ACCESS_TOKEN_SECRET''
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

############
# account3 #
############

consumer_key = '<CONSUMER_KEY>'
consumer_secret = '<CONSUMER_SECRET>'
access_token = '<ACCESS_TOKEN>'
access_token_secret = 'ACCESS_TOKEN_SECRET'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#create lists

followers = api.followers_ids('<FOLLOWERS_ACCT>')
friends = api.friends_ids('<FRIENDS_ACCT>')

print(followers)

count = 0
destroycount = 0

for f in friends:
    if f not in followers:
        api.destroy_friendship(f)
        print("Destroyed")
        destroycount = destroycount + 1
    print(destroycount)
    count = count + 1
    print(count)
    time.sleep(1)

