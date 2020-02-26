bag = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(str(v) + ' ' + k)
    print('Total number of items: ' + str(item_total))

displayInventory(bag)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory:
            inventory[addedItems[i]] += 1
        else:
            inventory[addedItems[i]] = 1
    return inventory

bag = addToInventory(bag, dragonLoot)

displayInventory(bag)