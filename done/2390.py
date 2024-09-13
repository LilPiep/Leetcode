def removeStars(s):
    stack = []
    for c in s:
        stack.append(c)
        if c == "*":
            stack.pop()
            stack.pop()
    return "".join(stack)

print(removeStars("leet**cod*e"))