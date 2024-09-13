def countBits(n):
    ans = []
    for i in range(n+1):
        bit = str(bin(i))
        bit = bit[2:]
        c = bit.count("1")
        ans.append(c)
    return ans

print(countBits(2))