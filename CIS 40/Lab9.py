import random
'''
a program for the childhood game of hangman. In this game, 
the player has a limited number of turns in which to guess 
all the letters of a mystery word. 
'''
def hangman(file):
    tries = 0
    limit = 10
    userGuess=[]
    typedList = []
    flag = True
    fin = open(file)
    line = random.randint(1,113809)
    #init the words and user input wordlist 
    #using list to store data and reading text file in a for loop by line 
    for words in range(line):
        guessWord = fin.readline().strip()
    for userInput in guessWord:
        userGuess.append('_')
    for userWrong in range(limit):
        typedList.append(' ')
    #print(guessWord) #Never won so I put this to cheat  
    #Check the tries PART 1
    while tries < limit and flag == True:
        print("".join(userGuess))
        print("Wrong guesses :", "".join(typedList), "\n")
        checkflag = False
        inputflag = False        
        while inputflag == False:
            character= input("Guess a letter :")
            if len(character) == 1:
                inputflag = True
        #Checking the user data is correctly solved PART 2
        if character in typedList:
            print("That letter has already been guessed!")
        else:
            for i in range(len(guessWord)):
                if character in guessWord[i]:
                    userGuess[i] = character
                    checkflag = True
            if checkflag == False and tries < limit:
                typedList[tries] = character
                tries +=1
        # As show the game result PART 3
        if tries >= limit:
            print("Better luck next time! The word was:", guessWord)
        elif ("".join(userGuess) == "".join(guessWord)):
            print("Congrats! You guessed it!", guessWord)
            flag = False
hangman("words.txt")

'''
Write a program for the childhood game of hangman. In this game, the player has a limited number of turns in which to guess all the letters of a mystery word. Your program must have the following features:

A randomly-selected mystery word from words.txt.
import random, then call random.randint(1,113809) in order to randomly select a number between 1 and the total number of lines in words.txt.

10 turns (unique WRONG letter guesses) for the player
A display (each turn) of the correctly guessed letters, in all their correct positions within the mystery word.
A display (each turn) of the incorrectly guessed letters.
A success message if the user wins.
A failure message if the user loses (10 wrong letters without guessing all the letters of the words).
A message if the user accidentally re-enters an already-guessed letter, whether that letter was correct or not. Note that the user gets this message whether the already-guessed letter was right or wrong. Also, any repeated wrong guesses should not be counted towards the 10-wrong-letter max.
To submit your assignment, simply upload your single ready-to-run file of Python code.

My solution is 60 lines long, many of which are blank lines. Below is some annotated output from me playing my game.
'''