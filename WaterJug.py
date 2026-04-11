x = int(input("Enter capacity of jug1: "))
y = int(input("Enter capacity of jug2: "))
target = int(input("Enter target: "))

visited = set()
stack = [(0,0)]

print("Steps:")
while stack:
    a, b = stack.pop()

    if (a, b) in visited:
        continue

    visited.add((a, b))
    print(a, b)

    if a == target or b == target:
        print("Target reached")
        break   

    stack.extend([
        (x, b), (a, y),     
        (0, b), (a, 0),     
        (max(0, a-(y-b)), min(y, b+a)),  
        (min(x, a+b), max(0, b-(x-a)))   
    ])