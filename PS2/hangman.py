# Problem Set 2, hangman.py
# Name: akgill
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
VOWELS = ['a', 'e', 'i', 'o', 'u']


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    to_display = []
    for letter in secret_word:
        if letter in letters_guessed:
            to_display.append(letter)
        else:
            to_display.append("_")
    
    return " ".join(to_display)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    to_display = []
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            to_display.append(letter)
    
    return " ".join(to_display)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    num_guesses = 6
    letters_guessed = []
    bad_guesses = 0
    while num_guesses > 0:
        # print beginning of turn info
        print("You have {num_guesses} guesses to solve this game of hangman.\n"
              .format(num_guesses=num_guesses))
        print("These are the letters you haven't guessed yet:\n {unguessed}"
              .format(unguessed=get_available_letters(letters_guessed)))
        
        # get and validate a newly guessed letter from the user and penalize
        # them if they give invalid inputs too many times
        new_guess = input("What letter would you like to guess?\n").lower()
        while (num_guesses > 0) and (
                not new_guess.isalpha()
                or len(new_guess) != 1
                or new_guess in letters_guessed):
            
            if new_guess in letters_guessed:
                print("You have already guessed '{guess}', so this is not a "
                      + "valid guess.\n".format(guess=new_guess))
            else:
                print("Sorry, that is not a valid guess. Please supply a "
                      + "single alphabetic character as a guess.\n")
            
            print(("This is warning #{num}. After three warnings, you will "
                  "lose a turn for each invalid guess.\n\n")
                  .format(num=bad_guesses+1))
            
            if bad_guesses >= 3:
                num_guesses -= 1
                print("You've had too many invalid guesses. As a penalty, you "
                      + "will lose one turn. You now only have {num_guesses} "
                      + "guesses left.".format(num_guesses=num_guesses))
            
            new_guess = input("What letter would you like to guess?\n").lower()
            bad_guesses += 1

        letters_guessed.append(new_guess)
        
        if new_guess in secret_word:
            print("{letter} is in this word!\n".format(letter=new_guess))
        else:
            print("{letter} is NOT in this word.\n".format(letter=new_guess))
            if new_guess in VOWELS:
                print("Incorrectly guessed vowels cost two turns.\n")
                num_guesses -= 2
            else:
                print("Incorrectly guessed consonants cost one turns.\n")
                num_guesses -= 1
            
        print("Current guessed word:\n\n{guessed}\n\n"
              .format(guessed=get_guessed_word(secret_word, letters_guessed)))
        
        if is_word_guessed(secret_word, letters_guessed):
            print("YOU WIN!!!")
            return

        
    print("Sorry, you lost. The secret word was:\n\n{secret}"
          .format(secret=secret_word))



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
