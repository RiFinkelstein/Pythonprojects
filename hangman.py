import random

# list of words to choose from
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# pick a random word from the list
word = random.choice(words)

# set up the game
max_guesses = 6
current_guesses = 0
letters_guessed = []

# game loop
while current_guesses < max_guesses:
    # display the current state of the word
    display_word = ''
    for letter in word:
        if letter in letters_guessed:
            display_word += letter
        else:
            display_word += '_'
    print(display_word)
    
    # get a guess from the player
    guess = input('Guess a letter: ').lower()
    
    # check if the guess is valid
    if len(guess) != 1 or not guess.isalpha():
        print('Please enter a single letter.')
        continue
    if guess in letters_guessed:
        print('You already guessed that letter.')
        continue
    
    # add the guess to the list of letters guessed
    letters_guessed.append(guess)
    
    # check if the guess is correct
    if guess in word:
        print('Correct!')
        if all(letter in letters_guessed for letter in word):
            print('You win!')
            break
    else:
        print('Incorrect.')
        current_guesses += 1
    
# end of game loop
if current_guesses == max_guesses:
    print('You lose. The word was', word)
