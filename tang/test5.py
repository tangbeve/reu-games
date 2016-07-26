
import random

def Playing():
    listOfWords = ["python", "C ++", "ruby","java"]
    print ("The category is programming langugaes!!!!")

    again = True #variable created
    while again: #created a loop

           guessWord = random.choice(listOfWords) #choses a randomly out of the words in the variable listofWords
           board = "-" * len(guessWord) #prints how many letters theirn are in the randomly chosen word in - format
           alreadySaid = set()
           mistakes = 6 # the msitakes start at 6

           print(" ".join(board)) # joining other letters/ replace - wirh the actual letteers

           guessed = False
           while not guessed and mistakes > 0:

               guess = input("Guess a letter: ") #tells you to guess a letter and input it
               if guess in guessWord: #if the leter you guessed is in the randomly selected word
                   alreadySaid.add(guess) #add it to whats already been said
                   board = "".join([char if char in alreadySaid else "-" for char in guessWord]) # join them
                   if board == guessWord:
                       guessed = True
               else:
                   mistakes -= 1 # minuses 1 from the value of mistakes (7) if you get the guess wrong
                   print("Nope.", mistakes, "mistakes left.") # if what you guessed is wrong then print nope and how many mistakes are remaining

               print(" ".join(board))

           print('well done')
           again = (input("Would you like to go again [y/n]: ").lower() == 'y') # asks if you want to go again -- changes it to lower cap

Playing() # displays Playing() whithout you typing in Playing() for it to appear