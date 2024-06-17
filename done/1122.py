def relativeSortArray(arr1, arr2):
    arr1.sort(key=lambda x: (0, arr2.index(x)) if x in arr2 else (1, x))
    return arr1