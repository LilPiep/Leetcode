s1 = "aa"
s2 = "aab"


def canConstruct(ransomNote, magazine):
    inventory = {}
    for c in magazine:
        if c not in inventory:
            inventory[c] = 1
        else:
            inventory[c] += 1
    for c in ransomNote:
        if c in inventory:
            inventory[c] -= 1
        else:
            return False
    for key in inventory:
        if inventory[key] < 0:
            return False
    return True


print(canConstruct(s1, s2))
