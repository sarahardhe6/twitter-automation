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
    "Hello, I am Rep. #FakeDenham and I am here to take away your healthcare.",
    "I vote with my party 98% of the time, in case you think I care about my constituents.",
    "I am Rep. #FakeDenham and I responsible for turning the Central Valley into a dustbowl.",
    "Sorry Modesto, I am your Congressman but I totally forgot about that when I gave tax cuts to the ultrarich again.",
    "I've said it ten time already... #JoshHarder wiped the floor with me at the debate. #FakeDenham",
    "I may be a #fakefarmer but at least I took away your healthcare.",
    "Well what do you say #FakeDenham I'd like to see a little engagement from you on this platform.",
    "Water Wealth Contentment Health for #FakeDenham and his buddies huh?",
    "My name is #FakeDenham and I went to school in #SALINAS",
    "Hello constituents I am Congressman #FakeDenham and I am not from #CD10",
    "My name is #FakeDenham and I have never been to a taco truck",
    "Hello, I am #FakeDenham and I vote with my party 98% of the time. I can't think for myself! Sorry not sorry!",
    "I wonder what #FakeDenham stores in the empty warehouse he calls a 'local business'",
    "As your Congressman, I, #FakeDenham, hereby do sell all of the #CentralValley's water and order it to be shipped to my farm in #Salinas",
    "It might be hard for me to understand the issues affecting my constitutents because I am not from this district.",
    "I am your Congressman #FakeDenham and I did not go to a Central Valley school.",
    "I am your Congressman #FakeDenham and my number does not start with (209)",
    "Waaah Waaah waaaaah I'm your crybaby Congressman #FakeDenham after getting rekt by #joshharder at the debate"
]

tags = [
    " #Modesto",
    " #Tracy",
    " #Ceres",
    " #209",
    " #plasticdenham",
    " #fakefarmer",
    " #centralvalley",
    " #waterfight",
    " #Ripon",
    " #Salida",
    " #BlueWave",
    " #Midterms",
    " #JoshHarder",
    " #BlueTsunami",
    " #RedToBlue",
    " #crybabyDenham",
    " #CD10",
    " #CA10"
    " #DumpDenham"
]
imageslist = [
    "IMG_1049.JPG",
    "IMG_1050.JPG",
    "IMG_1051.JPG",
    "IMG_1052.JPG",
    "IMG_1053.JPG",
    "IMG_1054.JPG",
    "IMG_1056.JPG",
    "IMG_1057.GIF",
    "IMG_1058.GIF",
    "IMG_1059.GIF",
    "IMG_1062.JPG",
    "IMG_1063.JPG",
    "IMG_1064.JPG",
    "IMG_1068.JPG",
    "IMG_1069.JPG",
    "IMG_1156.JPG",
    "IMG_1157.JPG",
    "IMG_1159.JPG",
    "IMG_1160.JPG"
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