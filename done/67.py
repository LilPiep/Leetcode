test1 = "11"
test2 = "1"


def addBinary(a, b):
    return str(bin(int(a, 2) + int(b, 2)))[2:]


print(addBinary(test1, test2))
