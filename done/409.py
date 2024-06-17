s = input()

ans = 0
inventory = {}
odd = False

for c in s:
    if c in inventory:
        inventory[c] += 1
    else:
        inventory[c] = 1
    
for c in inventory.values:
    if c % 2 == 0:
        ans += c
    else:
        ans += c - 1
        odd = True

if odd:
    print(ans + 1)
else:
    print(ans)