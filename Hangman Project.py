# Hangman Project

in_file = open("Words_List.txt", "rt") # open file Words_List.txt for reading text data
contents = in_file.read()         # read the entire file into a string variable
in_file.close()                   # close the file

contents = contents.split()         # contents is now a list of all words in the english dictionary

from random import randint      # importing randint from random to generate random_index

random_index = randint(0,len(contents)-1)       # INTEGER: generates a random_index to choose our word
secret_word = contents[random_index]        # STRING: secret_word is a string like 'coins'
length_secret_word = len(secret_word)       # INTEGER: takes the length of the string, secret_word       
number_of_guesses = 0                    # INTEGER: starts at 0, for every wrong guess it increases by 1
filter_guessed = []                # List which will occupy all the letters the user guesses, used to stop the user guessing the same letter twice
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

users_name = str(input("Welcome to Novica's game of Hangman... What is your name?: "))       #Introduction to the game asking for the users name

print("Good luck", users_name,"you're going to need it! Here is your random word, you have 6 guesses!")      #Work needs to be done here to include the user_name in the string output      

XXX = []        # Empty list of what will be the hidden secret word
for x in range(0,len(secret_word)):          # For loop converting XXX (the empty list) into a presentable format with the correct number of "_"s
    XXX.append("_")         
    
print(''.join(XXX))         # Printing the hidden word so the user can see how long the word is

while number_of_guesses < 6:        # While formula to keep the program running while the number_of_guesses < 6, the number of guesses decreases by 1 for every wrong guess
    if secret_word == ''.join(XXX):     # If statement to end the program if the working guess (XXX) equals the secret word
        print("Congratulations! You Win!")      # Congratulations statement if the user wins
        break                   # Break to stop the while loop from continuing to run if the user wins
    else:
        print("guesses left", 6 - number_of_guesses)        # Prints the number of guesses left by taking the difference with the number of guesses
        guess_letter = str(input("Guess letter: "))     # INPUT: setting the guess_letter variable equal to the letter the user guesses
        if guess_letter in filter_guessed:              # If statement to stop the user guessing a letter they have already guessed
            print("You've already guessed that letter!")
        elif guess_letter not in alphabet:              # If statement filtering out guesses that aren't in the alphabet
            print("Invalid input. You must enter a lowercase letter from the alphabet")
        else:
            if guess_letter in secret_word:             #If statement taking the path of a correct guess
                filter_guessed.append(guess_letter)     #Adds the guessed_letter to the list keeping track, filter_guessed
                indexes_of_guess_letter = []            #Resets the index_of_guessed_letters to an empty list. Crucial as if for example the previous run of the for loop left 3 entries in the list, but the latest run only leaves 1, it will leave an extra 2 unnecessary entries in our list
                indexes_of_guess_letter = [i for i, x in enumerate(secret_word) if x == guess_letter]           #List comprehension identifying the indexes of the guessed_letter in the secret_word
                if len(indexes_of_guess_letter) == 1:       #If statement taking the path of the simple case that the guessed_letter appears only once in the secret_word
                    XXX[indexes_of_guess_letter[0]] = guess_letter      # Updates the working guess with the new guessed_letter
                    print("Good guess! ", ''.join(XXX))                 # Prints "Good guess!" as the guessed_letter appeared in the secret_word once
                else:                                           # Else statement taking the path of the more complicated scenario that the guessed_letter appears multiple times in the secret_word
                    for index in indexes_of_guess_letter:               # For loop taking the index from the indexes_of_guess_letter
                        XXX[index] = guess_letter               # Replaces the working guess with the new guessed_letter
                    print("Excellent guess! ", ''.join(XXX))        # Prints "Excellent guess!" as the guessed_letter appeared in the secret_word more than once
            else:
                number_of_guesses += 1                  # Increments number_of_guesses by 1 for a wrong guess
                filter_guessed.append(guess_letter)
                print(guess_letter, " not in the secret word! Try again")       # Print statement saying that the guessed letter is not in the secret word

if number_of_guesses == 6:
    print("Unlucky, you lose! The secret word was", secret_word)
