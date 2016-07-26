list = [1,2,3,4,4]
print "Tha max value element:",max(list)

def mean(values):

    length = len(values)
    total_sum = 0
    for i in range(length):
        total_sum += values[i]
    total_sum = sum(values)
    average = total_sum/length
    return average

x = [1,2,3,4,4]
n = mean(x)

print(n)

list = [1,2,3,4,4]
list.reverse();
print "list:", list





  wordstring = {'A ','police','officer','found','a ','perfect','hiding','place','for', 'watching', 'for', 'speeding',
              'motorists','One','day', 'the','officer', 'was', 'amazed', 'when', 'everyone', 'was', 'under' ,'the','speed',
              'limit', 'so', 'he', 'investigated', 'and', 'found','the','problem','A','10', 'years', 'old', 'boy','was',
              'standing','on','the','side','of','the','road','with','a','huge','hand','painted','sign', 'more', 'investigative',
              'work', 'led', 'the', 'officer', 'to', 'the', 'boy’s', 'accomplice', 'another', 'boy', 'about', 100 ,'yards', 'beyond',
            'the', 'radar', 'trap','with','a','sign'}

wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print "String\n" + wordstring +"\n"
print "List\n" + str(wordlist) + "\n"
print "Frequencies\n" + str(wordfreq) + "\n"
print "Pairs\n" + str(zip(wordlist, wordfreq))