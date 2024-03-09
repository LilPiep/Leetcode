test = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
       [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
       ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
       [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
       [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


def isValidSudoku(board):
    # Are rows valid ?
    for row in board:
        check = []
        for i in range(9):
            if row[i] == '.' or (row[i] != '.' and row[i] not in check):
                check.append(row[i])
        if len(check) != 9:
            return False
    # Are columns valid ?
    for i in range(9):
        column = []
        for j in range(9):
            if board[j][i] == '.' or (board[j][i] != '.' and board[j][i] not in column):
                column.append(board[j][i])
        if len(column) != 9:
            return False
    # Are boxes valid ?
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            box = []
            for x in range(0, 3):
                for y in range(0, 3):
                    if board[x + i][y + j] in box and board[x + i][y + j] != '.':
                        return False
                    box.append(board[x + i][y + j])
    return True


print(isValidSudoku(test))
