from collections import deque
from itertools import permutations

# -------------------------------
# 1. BFS (User Input Graph)
# -------------------------------
from collections import deque

graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("Enter start node: ")

visited = set()
queue = deque([start])

print("BFS Traversal:")
while queue:
    node = queue.popleft()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph.get(node,[]):
            if neighbor not in visited:
                queue.append(neighbor)
print()


# ------------------------------- 
# 2. DFS
# -------------------------------
def dfs_util(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for n in graph.get(node, []):   # FIXED
            dfs_util(graph, n, visited)


graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node}: ").split()
    graph[node] = neighbors

start = input("Enter start node: ")

print("DFS Traversal:")
dfs_util(graph, start, set())
print()


# -------------------------------
# 3. Tic Tac Toe
# -------------------------------
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
            winner=False
            break
        player = "O" if player=="X" else "X"
    else:
        print("Invalid move")
if not winner:
    print("Draw!")



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

   

# -------------------------------
# 5. Water Jug
# -------------------------------

x = int(input("Enter capacity of jug1: "))
y = int(input("Enter capacity of jug2: "))
target = int(input("Enter target: "))

visited = set()
stack = [(0,0)]

print("Steps:")
while stack:
    a, b = stack.pop()
    if (a,b) in visited:
        continue
    visited.add((a,b))
    print(a, b)

    if a == target or b == target:
        print("Target reached")
        return

    stack.extend([
        (x,b),(a,y),(0,b),(a,0),
        (max(0,a-(y-b)), min(y,b+a)),
        (min(x,a+b), max(0,b-(x-a)))
    ])


# -------------------------------
# 6. TSP
# -------------------------------

n = int(input("Enter number of cities: "))
graph = []

print("Enter cost matrix:")
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

cities = list(range(n))
min_cost = float('inf')
bp=None
for perm in permutations(cities):
    cost = 0
    path=(0,)+perm(0, )
    for i in range(len(path)-1):
        cost+=graph[path[i]][path[i+1]]
    if cost<min_cost:
        min_cost=cost
        bp=path

print("Minimum Cost:", min_cost)
print("Best Path:", bp)


# -------------------------------
# 7. Tower of Hanoi
# -------------------------------
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, auxiliary, target, source)

n = int(input("Enter number of disks: "))
hanoi(n, 'A', 'C', 'B')
