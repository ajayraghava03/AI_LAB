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
def eight_puzzle():
    goal = "123456780"
    start = input("Enter initial state (use 0 for blank): ")

    def get_neighbors(state):
        moves = []
        i = state.index('0')
        swaps = {
            0:[1,3],1:[0,2,4],2:[1,5],
            3:[0,4,6],4:[1,3,5,7],5:[2,4,8],
            6:[3,7],7:[4,6,8],8:[5,7]
        }
        for j in swaps[i]:
            lst = list(state)
            lst[i], lst[j] = lst[j], lst[i]
            moves.append("".join(lst))
        return moves

    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal:
            print("Solved Path:", path)
            return
        visited.add(state)
        for n in get_neighbors(state):
            if n not in visited:
                queue.append((n, path+[n]))


# -------------------------------
# 5. Water Jug
# -------------------------------
def water_jug():
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
def tsp():
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

def run_hanoi():
    n = int(input("Enter number of disks: "))
    hanoi(n, 'A', 'C', 'B')
