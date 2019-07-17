###########
# imports #
###########

import markovify
import random

######################
# read in the corpus #
######################

with open('corpus1.txt') as file:
    text = file.read()

with open('mcdondalds.txt') as file:
    text2 = file.read()

#######################
# Generate the models #
#######################

model1 = markovify.Text(text, state_size=2)
model2 = markovify.Text(text, state_size=3)
mcds_model = markovify.Text(text2, state_size=2)
model3 = markovify.Text(text, state_size=2)
combo = markovify.combine([sabatino1, mcds_model], [30, 1])

################################
# word lists for text cleaning #
################################

wordlist1 = ['McDonalds','manager',"McDonald's"]
menu_items = ['McChicken','iced tea','burger']
customer_verbs = ['ordered','orders']
people = ['person','people']
mcdonalds_actions = ['service']
accounts = ['@account1', '@account2','@account3']

#################
# utility lists #
#################

sentences = []
no_people = []
cleaner = []
tweets = []
hashtags = ["#cityofmodesto","#modestocitycouncil","#mayorbrandvold","#modesto","@BillZoslocki","@brandvold4mayor","@KristiAhYou","#corruption","Modesto, CA", "#SR132", "@mayorsabatino","#sabatino","#conflictofinterest","@ridenourfor6th", "@tonymadrigal"]
media = [
    'http://www.backstorynews.com/',
    'http://www.backstorynews.com/about/',
    'http://www.backstorynews.com/letter-from-the-publisher-carmen-sabatino/',
    'http://www.backstorynews.com/category/mayors-commentary/',
    'http://www.backstorynews.com/news-feed/',
    'http://www.backstorynews.com/letter-from-city-auditor/',
    'http://www.backstorynews.com/author/carmenbackstorynews-com/',
    'http://www.backstorynews.com/and-they-call-this-justice/',
    'http://www.backstorynews.com/polling-problems/',
    'http://www.backstorynews.com/the-cast/',
    'http://www.backstorynews.com/judge-denies-motion-to-remove-das-office-from-modesto-bail-bonds-case/',
    'http://www.backstorynews.com/defense-attorney-wants-das-office-removed-from-modesto-bail-bonds-case/',
    'http://www.backstorynews.com/fladager-to-take-care-of-possible-investigator-federal-indictment/',
    'http://www.backstorynews.com/winning-elections/',
    'http://www.backstorynews.com/who-paid-for-the-zagaris-dossier/',
    'http://www.backstorynews.com/city-of-modesto-refuses-to-comply-with-public-records-request/',
    'http://www.backstorynews.com/im-back/',
    'http://www.backstorynews.com/author/topcop2005sbcglobal-net/',
    'http://www.backstorynews.com/breaking-news-petrulakis-and-demartini-renew-pac-with-10000-to-oppose-sabatino/',
    'http://www.backstorynews.com/city-of-modestos-hud-audit/',
    'http://www.backstorynews.com/bad-day-in-black-rock/',
    'http://www.backstorynews.com/mural-of-homeless-rick-leads-to-veiled-free-speech-threats-by-downtown-improvement-district/',
    'http://www.backstorynews.com/jeff-denham-trump/',
    'http://www.backstorynews.com/backstory-radio-is-growing/',
    'http://www.backstorynews.com/breaking-news-mayor-and-back-story-news-excluded-from-courtroom/',
    'http://www.backstorynews.com/recommended-reading/',
    'http://www.backstorynews.com/we-hope-you-had-the-most-wonderful-holiday-season/',
    'http://www.backstorynews.com/mayors-fact-sheet-police-interrogation/',
    'http://www.backstorynews.com/the-pass-we-give-that-pass-we-choke-on/',
    'http://www.backstorynews.com/notes-for-mayor-sabatino-on-police-retirement-abuse/',
    'http://www.backstorynews.com/letter-to-ag-jeff-sessions/',
    'http://www.backstorynews.com/coming-to-the-back-story-hypocrisy-hypocrite-and-hypocrites-on-monday-july-3rd/',
    'http://www.backstorynews.com/weep-at-the-dying-of-the-exclusionary-rule-in-our-justice-system/',
    'http://www.backstorynews.com/category/mayors-commentary/page/2/',
    'http://www.backstorynews.com/category/modesto/',
    'http://www.backstorynews.com/wp-content/uploads/2018/11/city-auditor-memo-from-the-17th.pdf',
    'http://www.backstorynews.com/author/carmenbackstorynews-com/page/2/',
    'http://www.backstorynews.com/author/carmenbackstorynews-com/page/15/',
    'http://www.backstorynews.com/category/stanislaus-county/',
    'http://www.backstorynews.com/category/frank-carson/',
    'http://www.backstorynews.com/category/frank-carson/stanislaus-county-frank-carson/',
    'http://www.backstorynews.com/wp-content/uploads/2018/10/mayor-campaign-article-smaller.pdf',
    'http://www.backstorynews.com/chickens-coming-home-to-roost/',
    'http://www.backstorynews.com/showtime-at-the-apollo/',
    'http://www.backstorynews.com/the-phoenix-arises-from-the-ashes-again/',
    'http://www.backstorynews.com/and-the-lies-go-on-1/',
    'http://www.backstorynews.com/justice-long-overdue-in-stanislaus-county-4/',
    'http://www.backstorynews.com/justice-long-overdue-in-stanislaus-county-3/',
    'http://www.backstorynews.com/justice-long-overdue-in-stanislaus-county-2/',
    'http://www.backstorynews.com/justice-long-overdue-in-stanislaus-county/',
    'http://www.backstorynews.com/happy-fails-to-you/',
    'http://www.backstorynews.com/saga-of-darlissa-dirk-2017/',
    'http://www.backstorynews.com/who-in-the-he-is-meyer-naves/',
    'http://www.backstorynews.com/dont-let-up-part-3/'
    ]

###################
# text generation #
###################

for i in range(100):
    sentence = str(combo.make_short_sentence(140))
    sentences.append(sentence)
    random_tags = [hashtags[random.randrange(len(hashtags))]
                   for item in range(4)]
    random_media = random.choice(media)
    tweet = sentence + " " + random_tags[0] + " " + random_tags[1] + " " + random_tags[2] + " " + random_tags[3] + " " + random_media
    print(tweet)

###################
# random hashtags #
###################

random_tags = [hashtags[random.randrange(len(hashtags))]
             for item in range(2)]

print(random_tags)

###################
# Construct Tweet #
###################

random_media = random.choice(media)

tweet = sentence + " " + random_tags[0] + " " + random_tags[1] + " " + random_media

print(tweet)

#################
# Write Article #
#################






##########################
# Clean Corpus Utilities #
##########################

for l in sentences:
    print(l)
    for p in modesto_persons:
        print(p)
        if p in l:
            z = str.replace(sentence, p, 'City of Modesto')
            no_people.append(z)

print(no_people)

for l in sentences:
    for p in modesto_persons:
        if p in sentence:
            z = str.replace(sentence, p, 'City of Modesto')
            no_people.append(z)

print(no_people)

for k in no_people:
    for p in modesto_persons:
        if p in sentence:
            z1 = str.replace(sentence, p, 'City Council')
            cleaner.append(str.replace(z1))

print(cleaner)

    for k in modesto_persons:
        if k not in sentence:
            no_people.append(sentence)
            pass
        else:
            sentences.append(sentence)
            pass
        pass
    pass

print(no_people)
print(sentences)

###########
# madlibs #
############


for word in wordlist1:
    if word in old_text:
        new_text = str.replace(old_text, word, 'lol1')
        print(new_text)


for word in menu_items:
    if word in old_text:
        new_text = str.replace(old_text, word, 'lol2')
        print(new_text)

for word in mcdonalds_actions:
    if word in old_text:
        new_text = str.replace(old_text, word, 'lol3')
        print(new_text)

for word in customer_verbs:
    if word in old_text:
        new_text = str.replace(old_text, word, 'lol4')
        print(new_text)