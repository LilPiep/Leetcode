def spiralMatrixIII(rows, cols, rStart, cStart):
    ans = []
    diri, dirj = 0, 1
    twice = 2
    r = rStart
    c = cStart
    moves = 1
    next_moves = 2

    while len(ans) != rows*cols:
        if (-1 < r < rows) and ( -1 < c < cols):
            ans.append([r,c])
        r += diri
        c += dirj
        moves -= 1
        if moves == 0:
            diri, dirj = dirj, -diri 
            twice -= 1
            if twice == 0:
                twice = 2
                moves = next_moves
                next_moves += 1
            else:
                moves = next_moves - 1
    return ans

print(spiralMatrixIII(1,4,0,0))