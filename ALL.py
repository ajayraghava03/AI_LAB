
# -------------------------------
# 4. 8 Puzzle
# -------------------------------

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], board[i+1], board[i+2])
    print()

board = [1,2,3,4,0,6,7,5,8]

while True:
    print_board(board)

    if board == [1,2,3,4,5,6,7,8,0]:
        print("Puzzle Solved!")
        break

    move = input("Move (w=up, s=down, a=left, d=right): ")

    pos = board.index(0)

    if move == "w" and pos not in [0,1,2]:
        board[pos], board[pos-3] = board[pos-3], board[pos]

    elif move == "s" and pos not in [6,7,8]:
        board[pos], board[pos+3] = board[pos+3], board[pos]

    elif move == "a" and pos not in [0,3,6]:
        board[pos], board[pos-1] = board[pos-1], board[pos]

    elif move == "d" and pos not in [2,5,8]:
        board[pos], board[pos+1] = board[pos+1], board[pos]

    else:
        print("Invalid move!")

   
