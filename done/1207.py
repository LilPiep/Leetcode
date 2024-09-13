def uniqueOccurences(arr):
    keeptrack = {}
    for n in arr:
        if n in keeptrack:
            keeptrack[n] += 1
        else:
            keeptrack[n] = 1
    return len(keeptrack) == len(set(keeptrack.values()))

print(uniqueOccurences([1,2,2,1,1,3]))