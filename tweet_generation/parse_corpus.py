newlines = []
wordlist = ['McDonalds','McMuffin','egg McMuffin','mcdonalds','mcds']

with open('mcds.txt') as file:
    text = file.readlines()
    print(text)

    for line in text:
        for word in line:
            if word in {'McDonalds','mcdonalds', 'mcds'}
                newstring = str.replace(line, word, 'lol')
                print(newstring)




