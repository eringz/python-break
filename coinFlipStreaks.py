'''
    Try flip a coin 100 times that write down 'H' as Heads and 'T' as Tails.
    Write a program that randomly generated list of heads and tails with the following:
        Generated 10, 000 times
        Find out how often a streak of either six heads or six tails come up randomly 
'''



import random
numberOfStreaks = 0
experimentLength = 10000
coinFlipList = []
headStreak = ['H', 'H', 'H', 'H', 'H', 'H']
tailStreak = ['T', 'T', 'T', 'T', 'T', 'T']

for experimentNumber in range(experimentLength):
 # Code that creates a list of 100 'heads' or 'tails' values.
    for i in range(100):
        coinFlipList.append(random.choice(['H', 'T']))
 # Code that checks if there is a streak of 6 heads or tails in a row.
# print('from this list: %s' % (coinFlipList))
for x in range(len(coinFlipList)-5):
    # print(coinFlipList[x:x+6], end=': ' )
    # print(coinFlipList[x:x+6] == headStreak or coinFlipList[x:x+6] == tailStreak  )
    if coinFlipList[x:x+6] == headStreak or coinFlipList[x:x+6] == tailStreak:
        numberOfStreaks += 1
     
totalAttempts = experimentLength *  100
print('Number of Streaks: %s' % (numberOfStreaks)) 
print('Total Attempts: %s' % totalAttempts)
# print('Chance of streak: %s%%' % (numberOfStreaks / 100))   
print('Chance of streak: %s%%' % (numberOfStreaks / (totalAttempts * 100) ))   
