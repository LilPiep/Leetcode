case1 = [1,2,3,1]
case2 = [1,0,1,1]
case3 = [1,2,3,1,2,3]

k1 = 3
k2 = 1
k3 = 2

def containsNearbyDuplicate(nums, k):
    inventory = {}
    for i in range(len(nums)):
        if nums[i] not in inventory:
            inventory[nums[i]] = [i]
        else:
            inventory[nums[i]].append(i)
    print(inventory)
    for key in inventory:
        if len(inventory[key]) > 1:
            for i in range(len(inventory[key]) - 1):
                if abs(inventory[key][i] - inventory[key][i+1]) <= k:
                    return True
    return False


print(containsNearbyDuplicate(case3, k3))