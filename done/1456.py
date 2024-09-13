def maxVowels(s, k):
    vowels = {"a", "e", "i", "o", "u"}
    current = sum(1 for char in s[:k] if char in vowels)
    max_vowels = current

    for i in range(k, len(s)):
        if s[i] in vowels:
            current += 1
        if s[i - k] in vowels:
            current -= 1
        max_vowels = max(max_vowels, current)

    return max_vowels

print(maxVowels("abciiidef", 3))