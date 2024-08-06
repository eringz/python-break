# I am thinking of a number between 1 and 20
#take up to 7 gueses
#conditions are 'Your guess is too low.', 'Your guess is too high.' until we guess a number a number 1 to 20

import random

secretNumber = random.randint(1, 20)

print('Take a guess from 1 to 20 up to 7 times only.')

for gt in range(1, 7):
    guess = int(input('So what is the number? '))
    if guess < secretNumber:
        print('Your guess is too low.')
    elif > secretNumber
        print('Your guess is to high.')
    else:
        break

if guess == secretNumber:
    print('Good job! you guess it right for only' + gt + ' attempt(s)')
else:
