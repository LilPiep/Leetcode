test = [9, 9, 9]


def plusOne(digits):
    i = -1
    check = 0
    while check == 0:
        for digit in digits:
            if digit != 9:
                check = 1
        break
    if check == 0:
        digits.insert(0, 0)
    while digits[i] == 9:
        digits[i] = 0
        i -= 1
    digits[i] += 1
    return digits


print(plusOne(test))
