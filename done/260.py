t = [1,2,1,3,2,5]
inventory = {}
for n in t:
    if n not in inventory:
        inventory[n] = 1
    else:
        del inventory[n]
print(list(inventory.keys()))