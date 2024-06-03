n1 = 19
n2 = 2

def isHappy(n):
    if n == 1 or n == 7:
        return True
    if n < 10 and n not in [1, 7]:
        return False
    else:
        n = [int(a) for a in str(n)]
        print(n)
        new = 0
        for digit in n:
            new += digit**2
        return isHappy(new)

print(isHappy(n1))