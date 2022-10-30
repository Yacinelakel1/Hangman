import random
import string 
from visual_hangman import hangman
def read_file():
    with open('word.txt','r') as file :
           words = [word for word in file]
    file.close()   
    new_words = [item.strip('\n') for item in words]
    return new_words

def get_valid_word():
    word = random.choice(read_file())
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7
    i = 0
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
    
        print()

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('Take away life \n',hangman[i])
                i =+1
                print('\nYour letter,', user_letter, 'is not in the word.')
                

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(hangman[6])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')

get_valid_word()

         

    

