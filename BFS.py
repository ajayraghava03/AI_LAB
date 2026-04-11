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