# Uses code from https://github.com/dcbriccetti/python-lessons/blob/master/Harder/hangman.py

from hangmanwords import words
from random import choice

word = choice(words)
correct = set()
wrong = set()
MAX_GUESSES = len(word)
num_guesses = 0

while num_guesses < MAX_GUESSES:
    print(MAX_GUESSES - num_guesses, 'guesses left')
    clue = [letter if letter in correct else '-' for letter in word]
    print(' '.join(clue))
    if wrong:
        print('Wrong:', ' '.join(sorted(list(wrong))))

    guess = input('Guess? ')
    num_guesses += 1

    if guess == word:
        print('Right!')
        break
    if len(guess) > 1:
        print('Wrong')
    else:
        if guess in correct or guess in wrong:
            print('You already guessed that')
        else:
            if guess in word:
                print('Right')
                correct.add(guess)
            else:
                print('Wrong')
                wrong.add(guess)
                draw_functions[len(wrong) - 1]()

