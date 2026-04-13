from itertools import permutations

n = int(input("Enter number of cities: "))
graph = []

print("Enter cost matrix:")
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

cities = list(range(1, n))   
min_cost = float('inf')
bp = None

for perm in permutations(cities):
    path = (0,) + perm + (0,)  
    cost = 0

    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i+1]]

    if cost < min_cost:
        min_cost = cost
        bp = path

print("Minimum Cost:", min_cost)
print("Best Path:", bp)

#n = 4

# Cost Matrix:
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
