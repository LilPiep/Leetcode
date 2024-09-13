def reverseParentheses(s):
    keeptrack = []
    for char in s:
        if char == ')':
            rev = ""
            while keeptrack and keeptrack[-1] != '(':
                rev += keeptrack.pop()
            if keeptrack:
                keeptrack.pop() 
            for c in rev:
                keeptrack.append(c)
        else:
            keeptrack.append(char)

    return ''.join(keeptrack)
    

print(reverseParentheses("(u(love)i)"))