from random import randint
import emoji
print('***GUESS THE NUMBER***\n')
r = randint(1, 100)
guess = 0
while guess != r:
    guess = int(input('Guess: '))
    if guess == r:
       print(emoji.emojize('\n :trophy: Winner! :trophy:', use_aliases=True))
    else:
        if guess > r:
            print('Try a lower number')
        else:
            print('Try a higher number')
print('\n{} END {}'.format('='*10, '='*10,))
