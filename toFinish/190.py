test = "00000010100101000001111010011100"

def reverseBits(n):
    new = ""
    i = -1
    while i > -33:
        new += n[i]
        i -= 1
    return int(new,2)

print(reverseBits(test))