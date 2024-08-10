allGuests = {
    'Alice': {'apples': 5, 'pretzels': 12},
    'Bob': {'ham sandwiches': 3, 'apples': 2},
    'Carol': {'cups': 3, 'apple pies': 1}
}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things beign brought:')
print('- Apples                 %s' % totalBrought(allGuests, 'apples'))
print('- Cups                   %s' % totalBrought(allGuests, 'cups'))
print('- Cakes                  %s' % totalBrought(allGuests, 'cakes'))
print('- Ham Sandwiches         %s' % totalBrought(allGuests, 'ham sandwiches'))
print('- Apple Pies             %s' % totalBrought(allGuests, 'apple pies'))
