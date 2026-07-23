def missionaries_cannibals_dldfs(M, C, K, limit):
    initial_state = (M, C, 0)   # (Missionaries Left, Cannibals Left, Boat)
    goal_state = (0, 0, 1)
    S = []
    S.append((initial_state, [], 0))
    moves = []
    for m in range(K + 1):
        for c in range(K + 1):
            if 1 <= m + c <= K:
                moves.append((m, c))
    while S:
        (ML, CL, B), path, depth = S.pop()
        if (ML, CL, B) == goal_state:
            return path + [(ML, CL, B)]
        if depth >= limit:
            continue
        visited_in_path = set(path)
        visited_in_path.add((ML, CL, B))
        for m, c in reversed(moves):
            if B == 0:      # Boat moves Left -> Right
                ML_new = ML - m
                CL_new = CL - c
                B_new = 1
            else:           # Boat moves Right -> Left
                ML_new = ML + m
                CL_new = CL + c
                B_new = 0
            new_state = (ML_new, CL_new, B_new)
            if 0 <= ML_new <= M and 0 <= CL_new <= C:
                if ML_new == 0 or ML_new >= CL_new:
                    MR = M - ML_new
                    CR = C - CL_new
                    if MR == 0 or MR >= CR:
                        if new_state not in visited_in_path:
                            S.append((new_state, path + [(ML, CL, B)], depth + 1))
    return "No Solution Within Depth Limit"

M = int(input("Enter the number of Missionaries: "))
C = int(input("Enter the number of Cannibals: "))
K = int(input("Enter the Boat Capacity: "))
limit = int(input("Enter the Depth Limit: "))

solution = missionaries_cannibals_dldfs(M, C, K, limit)
if solution == "No Solution Within Depth Limit":
    print(solution)
else:
    print("\nSolution Path:")
    for step in solution:
        print(step)