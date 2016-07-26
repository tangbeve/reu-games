import random

articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL","Dog")
verbs = ("HIT", "SAW", "LIKED","PLAYED")
prepositions = ("WITH", "BY")

def sentence():

     return nounPhrase() + " " + verbPhrase()

def nounPhrase():

    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():

    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():

    return random.choice(prepositions)+ " " + nounPhrase()

def main():

    number = input("Enter the number of sentences: ")
    for count in xrange(0, number):
        print sentence()

main() 