def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
    if len(bloomDay) < m*k:
        return -1
    left, right = 1, max(bloomDay)
    while left < right:
        mid = left + (right - left) // 2
        if self.feasible(bloomDay, mid, m, k):
            right = mid
        else:
            left = mid + 1
    return left

def feasible(self, bloomDay, days, m, k):
    bouquets, flowers = 0, 0
    for bloom in bloomDay:
        if bloom > days:
            flowers = 0
        else:
            bouquets += (flowers + 1) // k
            flowers = (flowers + 1) % k
    return bouquets >= m


print(minDays(bloomDay=[1,10,3,10,2],m=3,k=1))