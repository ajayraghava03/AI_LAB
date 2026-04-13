from collections import deque

def monkey_banana():

    monkey = "door"
    box = "window"
    banana = "middle"

    start = (monkey, box, False, False)  
    # (monkey_pos, box_pos, on_box, has_banana)

    queue = deque([start])
    visited = set([start])

    while queue:
        monkey, box, on_box, has_banana = queue.popleft()

        print("State:", (monkey, box, on_box, has_banana))

        # Goal
        if has_banana:
            print("Goal Achieved!")
            return

        # Step 1: Move to box
        if monkey != box:
            new_state = (box, box, False, has_banana)

        # Step 2: Push box under banana
        elif box != banana and not on_box:
            new_state = (banana, banana, False, has_banana)

        # Step 3: Climb box
        elif not on_box:
            new_state = (monkey, box, True, has_banana)

        # Step 4: Grab banana
        else:
            new_state = (monkey, box, True, True)

        if new_state not in visited:
            queue.append(new_state)
            visited.add(new_state)


monkey_banana()
