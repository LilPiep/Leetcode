def largestAltitude(gain):
    tot = [0]
    for g in gain:
        tot.append(tot[-1]+g)
    return(max(tot))

print(largestAltitude([-5,1,5,0,-7]))