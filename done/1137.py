def tribonacci(n):
    @cache
    def t(n):
        if n==0: return 0
        if n<=2: return 1
        return t(n-1)+t(n-2)+t(n-3)
    return t(n)

print(tribonacci(4))