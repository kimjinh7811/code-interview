def delete_check(m, n, board, y, x):
    if board[y][x] == ' ':
        return False

    if (board[y][x] == board[y][x+1]) and (board[y][x] == board[y+1][x]) and \
       (board[y][x] == board[y+1][x+1]) :
        return True
    else:  
        return False

def get_del_candidate(m, n, board):
    del_cand = []
    for y in range(len(board)-1):
        for x in range(len(board[y])-1):
            if delete_check(m, n, board, y, x):
                del_cand.append((y, x))
    return del_cand

def delete_block(board, y, x):
    board[y][x:x+2] = '  '
    board[y+1][x:x+2] = '  '

def drop_block(board):
    for y in range(1, len(board)):
        for x in range(len(board[y])):
            if board[y][x] == ' ':
                for i in range(y):
                    board[y-i][x] = board[y-i-1][x]
                board[0][x] = ' '

def del_calc(board):
    del_cnt = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == ' ':
                del_cnt += 1
    return del_cnt

def solution(m, n, board):
    board = [list(board[i]) for i in range(len(board))]
    while True:
        del_cand = get_del_candidate(m, n, board) 
        
        if not del_cand:
            break

        for cand in del_cand:
            delete_block(board, *cand)

        drop_block(board)
    answer = del_calc(board)
    return answer

test_case = [
    [4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]],
    [6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]]
]

for t in test_case:
    print(solution(*t))