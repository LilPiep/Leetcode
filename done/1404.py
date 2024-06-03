s = str(input())
oe = int(s,2)
cpt = 0
while oe != 1:
    if oe % 2 == 1:
        oe += 1
    else:
        oe = oe/2
    cpt += 1
print(cpt)