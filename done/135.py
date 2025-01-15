def candy(ratings):
    children = len(ratings)
    tot_candies = [1] * children
    for i in range(1, children):
        if ratings[i] > ratings[i-1]:
            tot_candies[i] = tot_candies[i - 1] + 1
    for i in range(children-2,-1,-1):
        if ratings[i] > ratings[i + 1]:
            tot_candies[i] = max(tot_candies[i], tot_candies[i + 1] + 1)
    return sum(tot_candies)

print(candy([1,0,2]))