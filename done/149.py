def maxPoints(points):
    if len(points) == 1: return 1
    ans = 2
    for i in range(len(points) - 1):
        current_max = 2 
        for j in range(i + 1, len(points)):
            current = 2 
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            
            for k in range(j + 1, len(points)):
                dx_k = points[k][0] - points[i][0]
                dy_k = points[k][1] - points[i][1]
                if dy * dx_k == dy_k * dx:
                    current += 1
            current_max = max(current_max, current)
        ans = max(ans, current_max)
    return ans

print(maxPoints([[1,1],[2,2],[3,3]]))