test = "([}}])"


def isValid(s):
    s = [*s]
    if len(s) % 2 != 0:
        return False
    verif = {"(": ")", "[": "]", "{": "}"}
    verif_inv = {")": "(", "]": "[", "}": "{"}
    pile = []
    for element in s:
        if (element in verif_inv) and not pile:
            return False
        if element in verif:
            pile.append(element)
        if element in verif_inv:
            if pile[-1] == verif_inv[element]:
                pile.pop()
            else:
                return False
    if not pile:
        return True
    else:
        return False


print(isValid(test))
