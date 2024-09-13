from collections import Counter

def closeStrings(word1, word2):
    if len(word1) == len(word2):
        if set(word1) == set(word2):
            if list(Counter(word1)).sort() == list(Counter(word2)).sort():
                return True
    return False

print(closeStrings("abc","bca"))