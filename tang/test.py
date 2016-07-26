dict= {'Tangee': 6, 'Hagen': 5, 'Charles':7}
lengths = []
for dict in dict:
    lengths.append(len(dict))

print lengths



names = {'Tangee': 6, 'Hagen': 5, 'Charles':7}
keys = names.keys()
values = names.values()

print("Keys:")
print(keys)
print(len(keys))

print("Values:")
print(values)
print(len(values))



d = {'Tangee': 6, 'Hagen': 5, 'Charles': 7}
for key in d:
    print key, 'have ', d[key], 'letters in the name'

    wordstring = 'it was the best of times it was the worst of times '
    wordstring += 'it was the age of wisdom it was the age of foolishness'

    wordlist = wordstring.split()

    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w))

    print "String\n" + wordstring + "\n"
    print "List\n" + str(wordlist) + "\n"
    print "Frequencies\n" + str(wordfreq) + "\n"
    print "Pairs\n" + str(zip(wordlist, wordfreq))
