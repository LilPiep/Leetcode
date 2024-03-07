test = "Hello world"

def lengthOfLastWord(s):
    s = s.split()
    return len(s[-1])

print(lengthOfLastWord(test))