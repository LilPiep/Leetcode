test = 4


def climbStairs(n):
    file = [1, 2]
    if n > 2:
        for i in range(2, n, 1):
            file.append(file[i-2] + file[i-1])
    return file[n-1]


print(climbStairs(test))
