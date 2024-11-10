def twoSum(numbers, target):
    pt = 0
    for n in numbers:
        pt += 1
        try:
            f = numbers[pt:].index(target - n)
            return [pt,pt+f+1]
        except ValueError: 
            continue

print(twoSum([0,0,3,4], 0))