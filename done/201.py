def rangeBitwiseAnd(left, right):
    return left & (-1 << (left ^ right).bit_length())

print(rangeBitwiseAnd(5,7))