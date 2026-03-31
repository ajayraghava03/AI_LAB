from collections import deque

def bfs_of_graph(V, adj, start):
    bfs = []                       
    visited = [False] * (V + 1)    

    q = deque()                    
    q.append(start)
    visited[start] = True

    while q:
        node = q.popleft()         
        bfs.append(node)

        for it in adj[node]:
            if not visited[it]:
                visited[it] = True
                q.append(it)

    return bfs

V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

adj = [[] for i in range(V + 1)]

print("Enter edges (u v):")
for i in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)   

start = int(input("Enter starting vertex: "))

result = bfs_of_graph(V, adj, start)

print("BFS Traversal:", *result)