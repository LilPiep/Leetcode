from math import factorial

def trailingZeroes(n):
    ans = 0
    while n > 0:
        n //= 5
        ans += n
    return ans

print(trailingZeroes(3))