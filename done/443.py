def compress(chars):
    l = len(chars)
    i = 0
    pt = 0
    while i < l:
        current = chars[i]
        count = 0
        while i < l and chars[i] == current:
            count += 1
            i += 1
        chars[pt] = current
        pt += 1
        if count > 1:
            for c in str(count):
                chars[pt] = c
                pt += 1
    return pt


print(compress(["a","a","b","b","c","c","c"]))