arr = [2,3,1,6,7]
cpt = 0
l = len(arr)
for i in range(l):
    for j in range(i+1,l):
        a=0
        for k in range(i,j):
            a ^= arr[k]
        b=0
        for k in range(j,l):
            b ^= arr[k]
            if a == b:
                cpt += 1
print(cpt)