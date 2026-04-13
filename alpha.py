def minimax(node, depth, alpha, beta, is_maximizing, tree):
    if node not in tree:
        return node
    children = tree[node]
    if is_maximizing:
        best = -1000
        for child in children:
            score = minimax(child, depth+1, alpha, beta, False, tree)
            best = max(best, score)
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f"Pruned at node {child}!")
                break
        return best
    else:
        best = 1000
        for child in children:
            score = minimax(child, depth+1, alpha, beta, True, tree)
            best = min(best, score)
            beta = min(beta, best)
            if beta <= alpha:
                print(f"Pruned at node {child}!")
                break
        return best

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [3, 5],
    'E': [2, 9],
    'F': [1, 7],
    'G': [4, 6]
}

result = minimax('A', 0, -1000, 1000, True, tree)
print(f"Best score: {result}")
