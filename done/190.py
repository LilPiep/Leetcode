test = "00000010100101000001111010011100"

def reverseBits(n):
    new = ""
    n = str(n)
    for b in reversed(n):
        new += b
    return int(new,2)

print(reverseBits(test))