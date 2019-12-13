def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        """""Combines a list into a dictionary."""""
        if addedItems[i] in inventory:
            inventory[addedItems[i]] += 1
        else:
            inventory.update({addedItems[i]: 1})
    return inventory


def displayInventory(inventory):
    """""Prints a summary of the items in the list."""""
    print('Inventory:')
    itemCount = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        itemCount += int(v)
    print('Total number of items: ' + str(itemCount))


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'gold coin', 'diamond', 'emerald']
inv = {'gold coin': 42, 'rope': 1}
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
