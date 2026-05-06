def missionaries_cannibals_dfs(M, C, K):
    initial_state = (M, C, 0)
    goal_state = (0, 0, 1)
    S = []
    S.append((initial_state, []))  # (state, path)
    visited = set()
    visited.add(initial_state)

    moves = []
    for m in range(K + 1):
        for c in range(K + 1):
            if 1 <= m + c <= K:
                moves.append((m, c))
    while S:
        (ML, CL, B), path = S.pop()
        if (ML, CL, B) == goal_state:
            return path + [(ML, CL, B)]
        for m, c in moves:
            if B == 0:
                ML_new = ML - m
                CL_new = CL - c
                B_new = 1
            else:
                ML_new = ML + m
                CL_new = CL + c
                B_new = 0
            new_state = (ML_new, CL_new, B_new)
            if 0 <= ML_new <= M and 0 <= CL_new <= C:
                if ML_new == 0 or ML_new >= CL_new:
                    MR = M - ML_new
                    CR = C - CL_new
                    if MR == 0 or MR >= CR:
                        if new_state not in visited:
                            visited.add(new_state)
                            S.append((new_state, path + [(ML, CL, B)]))

    return "No Solution"

M = int(input("Enter the number of Missionaries: "))
C = int(input("Enter the number of Cannibals: "))
K = int(input("Enter the Boat Capacity: "))
solution = missionaries_cannibals_dfs(M, C, K)
if solution == "No Solution":
    print(solution)
else:
    print("Solution path:")
    for step in solution:
        print(step)