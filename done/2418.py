def sortPeople(names, heights):
    
    journal = {}
    for i in range(len(names)):
        journal[heights[i]] = names[i]
    
    heights.sort(reverse=True)
    for ind in range(len(names)):
        h = heights[ind]
        names[ind] = journal[h]
    return names

print(sortPeople(["Mary","John","Emma"], [180,165,170]))