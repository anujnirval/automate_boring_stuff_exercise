stuff = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

def addToInventory(inventory,addedItems):
    newItem={}
    for i in range(len(addedItems)):
        if addedItems[i] not in newItem.keys():
            newItem[addedItems[i]]=addedItems.count(addedItems[i])
    for ke, ve in newItem.items():
        if ke in inventory.keys():
            inventory[ke]=inventory.get(ke) + ve
        else:
            inventory[ke]=ve
    return inventory

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
item=''
while True:
    item=raw_input("Enter the item to be added:(press 'e' to exit)\n")
    if item=='e':
        break;
    else:
        dragonLoot.append(item)
displayInventory(stuff)
print("Items to be added are: \n"+ str(dragonLoot))
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
