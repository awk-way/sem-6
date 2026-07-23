import math

def water_jug_dldfs(m, n, d, limit):
    stack = []
    stack.append((0, 0, 0, [], "Start"))  # jug1, jug2, depth, path, action
    solutions = []
    while stack:
        jug1, jug2, depth, path, action = stack.pop()
        path = path + [((jug1, jug2), action)]

        if jug1 == d or jug2 == d:
            solutions.append(path)
            continue

        if depth >= limit:
            continue

        next_states = []
        next_states.append((m, jug2, "Fill Jug A"))
        next_states.append((jug1, n, "Fill Jug B"))
        next_states.append((0, jug2, "Empty Jug A"))
        next_states.append((jug1, 0, "Empty Jug B"))
        pour = min(jug1, n - jug2)
        next_states.append((jug1 - pour, jug2 + pour, "Pour Jug A to Jug B"))
        pour = min(jug2, m - jug1)
        next_states.append((jug1 + pour, jug2 - pour, "Pour Jug B to Jug A"))

        visited_in_path = {state for state, _ in path}
        for new_j1, new_j2, act in reversed(next_states):
            if (new_j1, new_j2) not in visited_in_path:
                stack.append((new_j1, new_j2, depth + 1, path, act))

    if solutions:
        for i, solution in enumerate(solutions, 1):
            print(f"\nSolution {i}:")
            for step in solution:
                print(f"{step[1]:<20} -> {step[0]}")
    else:
        print("No solution found within the given depth limit.")

m = int(input("Enter capacity of Jug A: "))
n = int(input("Enter capacity of Jug B: "))
d = int(input("Enter target amount: "))
limit = int(input("Enter depth limit: "))
if d > max(m, n) or d % math.gcd(m, n) != 0:
    print("No solution possible")
else:
    water_jug_dldfs(m, n, d, limit)