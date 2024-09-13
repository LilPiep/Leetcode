def findTheWinner(n, k):
    oe = []
    for i in range(1,n+1):
        oe.append(i)
    pos = 0
    while len(oe) != 1:
        pos += k - 1 
        pos = pos % len(oe)
        del oe[pos]
    return oe[0]