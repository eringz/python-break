'''
    Write a program that randomly generated list of heads and tails with the following:
        Generated 10, 000 times
        Find out how often a streak of either six heads or six tails come up randomly 
'''

import random

def has_streak(coin_flips, streak_length):
    """Check if there is a streak of `streak_length` heads or tails in `coin_flips`."""
    heads = 'H' * streak_length
    tails = 'T' * streak_length
    
    return heads in coin_flips or tails in coin_flips

number_of_streaks = 0
streak_length = 6
num_experiments = 10000
num_flips = 100

for experiment_number in range(num_experiments):
    # Generate a list of 100 random 'heads' or 'tails' values
    coin_flips = ''.join(random.choice(['H', 'T']) for _ in range(num_flips))
    
    # Check if there is a streak of 6 heads or tails in a row
    if has_streak(coin_flips, streak_length):
        number_of_streaks += 1

# Print the chance of having at least one streak of 6 heads or tails
print('Chance of streak: %s%%' % (number_of_streaks / num_experiments * 100))
print(coin_flips)