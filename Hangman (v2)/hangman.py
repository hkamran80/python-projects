# Uses code from https://github.com/dcbriccetti/python-lessons/blob/master/Harder/hangman.py

from hangmanwords import words
from random import choice

word = choice(words)
correct = set()
wrong = set()
MAX_GUESSES = len(word)
num_guesses = 0

while num_guesses < MAX_GUESSES:
    print('Guesses Left: {0}'.format(MAX_GUESSES - num_guesses))
    clue = [letter if letter in correct else '-' for letter in word]
    print(' '.join(clue))
    if wrong:
        print('Wrong:', ' '.join(sorted(list(wrong))))

    guess = input('\nGuess? ')
    guess = guess.strip()
    num_guesses += 1

    if len(guess) > 1:
        if guess == word:
            print('You Win!')
            break
        else:
            print('Word not match.')
            continue

    if guess in correct or guess in wrong:
        print('You already guessed that')
        continue

    if guess in word:
        print('Right')
        correct.add(guess)
    else:
        print('Wrong')
        wrong.add(guess)
        # draw_functions[len(wrong) - 1]()

print('The word was:', word)