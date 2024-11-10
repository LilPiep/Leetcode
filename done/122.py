t1 = [1,2,3,4,5]

def maxProfit(prices):
    mylist = []
    cursor = 0
    tot = 0
    while cursor < (len(prices) - 1):
        if prices[cursor] < prices[cursor+1]:
            temp = []
            temp.append(prices[cursor])
            while cursor < len(prices) - 1 and prices[cursor] < prices[cursor+1]:
                temp.append(prices[cursor+1])
                cursor += 1
            mylist.append(temp)
        else:
            cursor += 1
    for sublist in mylist:
        tot += sublist[-1] - sublist[0]
    return tot


print(maxProfit(t1))