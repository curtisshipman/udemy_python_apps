#!/usr/bin/env python3

def get_word():
    # this function will ask the user for the word they ar going to try and guess.
    import getpass
    print("\nWelcome to The Guessing Game!\
        \nHave a friend type a word or phrase: ")
    wordInput = getpass.getpass(prompt="Entry: ", stream=None)
    return wordInput


def total_tries(word):
    # this function will decide how many tries you get.
    if len(word) > 20:
        totalTries = 7
    elif len(word) > 15:
        totalTries = 6
    else:
        totalTries = 5
    return totalTries


def guess_input():
    # this function will take the letter the user is trying to guess, update the set of used letters
    guess = input("Guess a letter: ").lower()
    return guess


def see_if_letter_has_been_used(guess, lettersGuessed):
    if guess in lettersGuessed:
        print("Letter already used.  Try a new letter.")
        print("Your last letter guessed is: '{}'".format(guess))
        print("All the letters you have guessed so far\n\t{}:".format(", ".join(lettersGuessed)))
        used = "y"
    #        guess_input()
    else:
        lettersGuessed.add(guess)
        used = "n"
    return lettersGuessed, used


def check_for_letter(word, guess, lives, guessedWord, lettersGuessed):
    # this fuction will check the letter guessed by the user and see if it is in the word or not.
    if guess in word:
        guessedWord = update_guessing_word(guess, word, guessedWord)
        print("\nYOU GOT ONE!")
        # print("{} tries left!".format(str(lives)))
    else:
        lives -= 1
        print("\n**** Ouch! **** '{}' was not in the word! Only {} tries left!".format(guess, str(lives)))
        # print("Only {} tries left!".format(str(lives)))
        # print("\n")
    return lives, guessedWord


def remove_spaces(word):
    # Function removes spaces from provided word or phrase
    guessedWord = ["*"] * len(word)
    for i in range(len(word)):
        if word[i] == " ":
            # print("replacing space" + str(i)) # testing my work by printing the index to see if it worked
            indexInWord = i
            guessedWord.pop(indexInWord)
            guessedWord.insert(indexInWord, " ")
    return guessedWord


def update_guessing_word(guess, word, guessedWord):
    # this fucntion will update the list being used to match with the word being guessed.
    for i in range(len(word)):
        if word[i] == guess:
            # print(i)  # testing my work by printing the index to see if it worked
            indexInWord = i
            guessedWord.pop(indexInWord)
            guessedWord.insert(indexInWord, word[i])
    return guessedWord


def play_game():
    # this plays the game by calling the other funtions.
    wordOriginal = get_word()
    word = list(wordOriginal.lower())
    correctLettersGuessed = remove_spaces(word)
    lettersGuessed = set()
    lives = total_tries(word)
    totalTries = lives
    print("The length of the word is: ", str(len(word)))
    print("You have a total of {} guesses.  Good Luck!\n".format(lives))
    while lives > 0:
        guess = guess_input()
        lettersGuessed, used = see_if_letter_has_been_used(guess, lettersGuessed)
        while used.lower() == "y":
            guess = guess_input()
            lettersGuessed, used = see_if_letter_has_been_used(guess, lettersGuessed)
        # else:
        #     continue 
        # correctLettersGuessed = update_guessing_word(guess, word, correctLettersGuessed)
        lives, correctLettersGuessed = check_for_letter(word, guess, lives, correctLettersGuessed, lettersGuessed)
        if correctLettersGuessed == word:
            print("You win!")
            print("Total lives used: {}".format(str(totalTries - lives)))
            print("The original word was '{}'".format(wordOriginal))
            print("The length of the word was: {}".format(str(len(word))))
            print("Your last letter guessed is: '{}'".format(guess))
            print("All the letters you have guessed so far\n\t{}:".format(", ".join(lettersGuessed)))
            print("\n\n")
            break
        else:
            # print("The word or phrase is '{}'.".format(word))
            print("The length of the word is: ", str(len(word)))
            print("Your total tries left: ", str(lives))
            print("Your last letter guessed is: ", guess)
            print("Your correct letters guessed so far: \n\t", str("".join(correctLettersGuessed)))
            print("All the letters you have guessed so far \n\t", str(", ".join(lettersGuessed)))
    if lives > 0:
        print("Great job!  Play again soon!")
    else:
        print("Too bad!  You can do better!")
        print("The word or phrase was '{}'.\n".format(wordOriginal))
    choice = input("Would you like to play again? (y/n): ")
    return choice


def main():
    choice = "y"
    while choice.lower() == "y":
        choice = play_game()
    else:
        print("\nThank you for playing.")
        print("\nBye!\n")

    # print("the word is ", str(word))
    # print("the length of the word is ", str(len(word)))
    # print(" total lives ", str(lives))
    # print("last letter guessed is ", guess)
    # print("correct letteres guessed so far \n", str(correctLettersGuessed))
    # print(" all letters guessed so far \n", str(lettersGuessed))
    # guesses = set()
    # print(word)

    # print(len(word))

    # while lives > 0:
    #     guess_input(guesses)
    #     guesses, guess = guess_input(guesses)
    #     check_for_letter(word, guess, lives)
    #     lives = check_for_letter(word, guess, lives)


if __name__ == "__main__":
    main()
