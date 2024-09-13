from collections import Counter

def kthDistinct(arr, k):
    counter = Counter(arr)
    for v in arr:
        if counter[v] == 1:
            k -= 1
            if k == 0:
                return v
    return ''

print(kthDistinct(["d","b","c","b","c","a"],2))