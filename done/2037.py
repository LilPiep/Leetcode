a = [12,14,19,19,12]
b = [19,2,17,20,7]

def minMovesToSeat(seats, students):
    seats.sort()
    students.sort()
    s = 0
    for i in range(len(seats)):
        s += abs(seats[i]-students[i])
    return(s)

print(minMovesToSeat(a,b))