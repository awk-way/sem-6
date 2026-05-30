def heuristic(state, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = \
                new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def print_state(state):
    for row in state:
        print(*row)

def hill_climbing(initial_state, goal):
    current = initial_state
    step = 1
    while True:
        current_h = heuristic(current, goal)
        print(f"\nSTEP {step}\nCurrent State: ")
        print_state(current)
        print(f"Heuristic = {current_h}")
        if current_h == 0:
            print("Goal State Reached!")
            return
        neighbors = generate_neighbors(current)
        print("\nGenerated States:")
        best_state = current
        best_h = current_h
        heuristics = []
        for neighbor in neighbors:
            h = heuristic(neighbor, goal)
            heuristics.append(h)
            if h < best_h:
                best_h = h
                best_state = neighbor
        for row in range(3):
            for neighbor in neighbors:
                print(*neighbor[row], end="\t\t")
            print()
        for h in heuristics:
            print(f"h = {h}", end="\t\t")
        print("\n")
        if best_h >= current_h:
            print("No better state found. Local Optimum Reached")
            return
        print("Chosen State For Next Iteration:")
        print_state(best_state)
        print(f"Heuristic = {best_h}")
        current = best_state
        step += 1

print("Enter Initial State (0 for blank):")
initial_state, goal_state = [], []
for i in range(3):
    row = list(map(int, input().split()))
    initial_state.append(row)
print("\nEnter Goal State (0 for blank):")
for i in range(3):
    row = list(map(int, input().split()))
    goal_state.append(row)
hill_climbing(initial_state, goal_state)