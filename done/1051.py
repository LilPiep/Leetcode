h = [1,1,4,2,1,3]

def heightChecker(heights):
    c = 0
    new_h = sorted(heights)
    for i in range(len(heights)):
        if new_h[i] != heights[i]:
            c += 1
    return c

print(heightChecker(h))