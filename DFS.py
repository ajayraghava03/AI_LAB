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