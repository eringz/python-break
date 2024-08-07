import random, time, copy

WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells:
nextCells = []

for x in range(WIDTH): # 60
    column = [] # Create a new column
    for y in range(HEIGHT): # 20
        if random.randint(0, 1) == 0:
            column.append('\033[32m1\033[0m') # Add a living cell
        else:
            column.append('\033[34m0\033[0m') # Add a dead cell
    nextCells.append(column) # nextCells is a list of column lists.

while True: # Main program loop.
    # print('\n\n\n\n\n') # Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells on the screen:
    for y in range(HEIGHT): #  20
        for x in range(WIDTH): # 60
            print(currentCells[x][y], end='') # Print the # or space.
        print()
    
    for x in range(WIDTH): # 60
        for y in range(HEIGHT): # 20
            # Get neighboring coordinates:
            # `% WIDTH` ensures leftCoord is always between o and WIDTH - 1
            leftCoord       =       ( x - 1 ) % WIDTH
            rightCoord      =       ( x + 1 ) % WIDTH
            aboveCoord      =       ( y - 1 ) % HEIGHT
            belowCoord      =       ( y + 1 ) % HEIGHT

            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '\033[32m1\033[0m':
                numNeighbors += 1                               # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '\033[32m1\033[0m':
                numNeighbors += 1                               # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '\033[32m1\033[0m':
                numNeighbors += 1                               # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '\033[32m1\033[0m':
                numNeighbors += 1                               # Left neighbor is alive.
            if currentCells[rightCoord][y] == '\033[32m1\033[0m':
                numNeighbors += 1                               # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '1\033[32m1\033[0m':
                numNeighbors += 1                               # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '\033[32m1\033[0m':
                numNeighbors += 1                               # Bottom neighbor is alive
            if currentCells[rightCoord][belowCoord] == '\033[32m1\033[0m':
                numNeighbors += 1                               # Bttom-right neighbor is alive.
            
            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '\033[32m1\033[0m' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '\033[32m1\033[0m'
            elif currentCells[x][y] == '\033[34m0\033[0m' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '\033[32m1\033[0m'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = '\033[34m0\033[0m'
    time.sleep(0.2) # Add a 1-second pause to reduce flickering.