
                    "You have lost. If you would like to play again then enter in the difficulty level, or 4 to exit")
                if (level != 4):
                    randomNewNumber = random.randint(0, len(listofwords) - 1)
                    guessNewWord = listofwords[randomNewNumber]
                if (level == 4):
                    sys.exit(0)

    if (level == '2'):
        print("You have selected the medium difficulty.")
        print("The word is: " + board(guesstheword))
        while (len(wrong) != 7):
            userGuess = input("Enter in the letter you want to guess: ")
            guessing(userGuess)
            if userGuess not in guesstheword:
                wrong.append(userGuess)
            print("You have " + str(len(wrong)) + " guesses. Guessed letters: " + str(wrong))
    if (level == '3'):
        print("You have selected the hard difficulty.")
        print("The word is: " + board (guesstheword))
        while (len(wrong) != 5):
            userGuess = input("Enter in the letter you want to guess: ")
            guessing(userGuess)
            if userGuess not in guesstheword:
                wrong.append(userGuess)
            print("You have " + str(len(wrong)) + " guesses. Guessed letters: " + str(wrong))


main()