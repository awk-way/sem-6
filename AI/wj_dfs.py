import math
def water_jug_dfs(m, n, d):
    stack = []
    visited = [[False]*(n+1) for _ in range(m+1)]
    stack.append((0, 0, 0, [], "Start"))
    visited[0][0] = True
    solutions = []
    while stack:
        jug1, jug2, count, path, action = stack.pop()
        path = path + [((jug1, jug2), action)]
        if jug1 == d or jug2 == d:
            solutions.append(path)
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
        for new_j1, new_j2, act in next_states:
            if not visited[new_j1][new_j2]:
                visited[new_j1][new_j2] = True
                stack.append((new_j1, new_j2, count+1, path, act))
    if solutions:
        for i, solution in enumerate(solutions, 1):
            print(f"Solution {i}:")
            for step in solution:
                print(f"   {step[1]:<20} -> {step[0]}")
            print()
    else:
        print("No solution possible")
m = int(input("Enter capacity of Jug A: "))
n = int(input("Enter capacity of Jug B: "))
d = int(input("Enter target amount: "))
if d > max(m, n) or d % math.gcd(m, n) != 0:
    print("No solution possible")
else:
    water_jug_dfs(m, n, d)
