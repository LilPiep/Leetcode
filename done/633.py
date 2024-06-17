from math import sqrt

def judgeSquareSum(c):
    divisor = 2
    while divisor * divisor <= c:
        if c % divisor == 0:
            exponentCount = 0
            while c % divisor == 0:
                exponentCount += 1
                c //= divisor
            if divisor % 4 == 3 and exponentCount % 2 != 0:
                return False
        divisor += 1
    return c % 4 != 3

print(judgeSquareSum(5))