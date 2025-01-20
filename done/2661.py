def firstCompleteIndex(self, arr, mat):
    m, n = len(mat), len(mat[0])
    position = {}
    for i in range(m):
        for j in range(n):
            position[mat[i][j]] = (i, j)
    row_count = [0] * m
    col_count = [0] * n
    for i, num in enumerate(arr):
        x, y = position[num] 
        row_count[x] += 1
        col_count[y] += 1
        if row_count[x] == n or col_count[y] == m:
            return i