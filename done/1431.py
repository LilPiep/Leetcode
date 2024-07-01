def kidsWithCandies(candies, extraCandies):
    ans = []
    for c in candies:
        ans.append(c + extraCandies >= max(candies))
    return ans

print(kidsWithCandies([2,3,5,1,3],3))