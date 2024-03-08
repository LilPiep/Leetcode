an = "ab"
na = "a"


def isAnagram(s, t):
    inventory = {}
    for c in s:
        if c not in inventory:
            inventory[c] = 1
        else:
            inventory[c] += 1
    for c in t:
        if c in inventory or (c in inventory and inventory[c] != 0):
            inventory[c] -= 1
        else:
            return False
    for key in inventory:
        if inventory[key] != 0:
            return False
    return True


print(isAnagram(an, na))
