def averageWaitingTime(customers):
    total_wait = 0
    current = 0
    for c in customers:
        if current < c[0]:
            current = c[0]
        finish_time = current + c[1]
        total_wait += (finish_time - c[0])
        current = finish_time
    return total_wait/len(customers)

print(averageWaitingTime([[1,2],[2,5],[4,3]]))