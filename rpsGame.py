# Rock, Paper, Scissors
# Displaying Wins, Losses, Ties
# player can enter the following move such as (r)ock, (p)aper (s)cissors or (q)uit
import random, sys

wins = 0
losses = 0
ties = 0

def computerPick():
    rn = random.randint(1, 3)
    if rn == 1:
        return 'ROCK'
    elif rn == 2:
        return 'PAPER'
    elif rn == 3:
        return 'SCISSORS'

def matchPick(pm, cm):
    if pm == cm:
        return 'TIE'
    elif pm == 'ROCK' and cm == 'SCISSORS':
        return 'WIN'
    elif pm == 'PAPER' and cm == 'ROCK':
        return 'WIN'
    elif pm == 'SCISSORS' and cm == 'PAPER':
        return 'WIN'
    elif pm == 'ROCK' and cm == 'PAPER':
        return 'LOSS'
    elif pm == 'PAPER' and cm == 's':
        return 'LOSS'
    elif pm == 'SCISSORS' and cm == 'ROCK':
        return 'LOSS'



print('Rock, Paper, Scissors')



while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        playerMove = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit ')
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            
            break
        print('Type one of r, p, s, or q')
    
    cm = computerPick()
    if playerMove == 'r':
        playerMove = 'ROCK'
        print(playerMove + ' versus ' + cm  )  
    elif playerMove == 'p':
        playerMove = 'PAPER'
        print('PAPER vs ' + cm )
    elif playerMove == 's':
        playerMove = 'SCISSORS'
        print('SCISSORS vs ' + cm )
    
    mp = matchPick(playerMove, cm)
    
    if mp == 'TIE':
        print('It is a tie!')
        ties += 1
    elif mp == 'WIN':
        print('You win!')
        wins += 1
    elif mp == 'LOSS':
        print('You loss!')
        losses += 1

 