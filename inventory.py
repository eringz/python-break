'''
    Fantasy Game Inventory
        You are creating a fantasy video game. The data structure to model the 
        player’s inventory will be a dictionary where the keys are string values 
        describing the item in the inventory and the value is an integer value 
        detailing how many of that item the player has. 
        For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
        means the player has 1 rope, 6 torches, 42 gold coins, and so on.
        Write a function named displayInventory() that would take any possible 
        “inventory” and display it like the following:

        Inventory:
            12 arrow
            42 gold coin
            1 rope
            6 torch
            1 dagger
            Total number of items: 62
'''

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
        print('%s  %s' % (v, k))
        item_total += v
    print("Total number of items: " + str(item_total))
# displayInventory(stuff)


def addToInventory(inventory, addedItems):
    # your code goes here
    item = ''
    for i in range(len(addedItems)):
        item = addedItems[i]
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1
            
                 
            
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ako']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)