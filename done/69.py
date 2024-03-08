test = 8


def mySqrt(x):
    if x == 0 or x == 1:
        return x
    borne_inf = 0
    while (borne_inf ** 2) < x:
        borne_inf += 1
    return borne_inf - 1


print(mySqrt(test))
