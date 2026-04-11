board = [" "] * 9

def print_board():
    for i in range(0, 9, 3):
        print(board[i:i+3])

def check_winner(p):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in wins)

player = "X"
winner=False
for _ in range(9):
    print_board()
    move = int(input(f"{player} move (0-8): "))
    if board[move] == " ":
        board[move] = player
        if check_winner(player):
            print_board()
            print(player, "wins!")
            winner=True
            break
        player = "O" if player=="X" else "X"
    else:
        print("Invalid move")
if not winner:
    print("Draw!")