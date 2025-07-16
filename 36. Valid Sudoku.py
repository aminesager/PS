board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def hasRec(num, i, j, board):
    row = board[i]
    column = [board[k][j] for k in range(9)]
    combined = row + column[:j] + column[j+1:]
    return combined.count(str(num)) == 0

def zone(num, i, j, board):
    a = (i // 3) * 3
    b = (j // 3) * 3
    count = 0
    for x in range(a, a + 3):
        for y in range(b, b + 3):
            if board[x][y] == str(num):
                count += 1
    return count <= 1

def result(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                continue
            actual = board[i][j]
            if not hasRec(actual, i, j, board) and not zone(actual, i, j, board):
                return False
    return True

print(result(board))