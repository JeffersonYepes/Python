from random import randint
from time import sleep
print('''========================================
        *** GUESS THE NUMBER ***        
========================================''')
r = randint(0, 5)
guess = int(input('Type a number between 0 and 5: '))
print('PROCESSING...')
sleep(2)
if guess == r:
    print('\nCongratulations! Winner!')
else:
    print('\nLOOOSER!')
    print('Correct number: {}'.format(r))
print('''
=========================================
             *** END ***        
=========================================''')
