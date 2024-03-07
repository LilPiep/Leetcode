test = 121


def isPalindrome(x):
    to_list = str(x)
    to_list = [*to_list]
    size = len(to_list)
    endroit = []
    envers = []
    for i in range(0, (size // 2), 1):
        endroit.append(to_list[i])
    if size % 2 == 0:  # ok
        for j in range(size - 1, (size // 2) - 1, -1):
            envers.append(to_list[j])
    else:
        for j in range(size - 1, (size // 2), -1):
            envers.append(to_list[j])
    if endroit == envers:
        return True
    return False


print(isPalindrome(test))
