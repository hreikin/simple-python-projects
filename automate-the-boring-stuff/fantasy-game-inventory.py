# Write a function named displayInventory() that would take any possible
# “inventory” and display it like the following:
# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62
# Hint: You can use a for loop to loop through all the keys in a dictionary.

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# Loops through the "keys" and "values" of the dictionary and prints them out 
# line by line. Then takes the "values" and converts them to an "int" and adds 
# them to the "item_total" variable.
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total = item_total + int(v)
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

# Imagine that a vanquished dragon’s loot is represented as a list of strings
# like this:
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# Write a function named addToInventory(inventory, addedItems) , where the
# inventory parameter is a dictionary representing the player’s inventory (like
# in the previous project) and the addedItems parameter is a list like dragonLoot .
# The addToInventory() function should return a dictionary that represents the
# updated inventory. Note that the addedItems list can contain multiples of the
# same item.

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)