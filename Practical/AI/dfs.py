def dfs(graph, n):
    visited, res, stck = [False] * n, [], []
    s = 0
    stck.append(s)
    while stck:
        u = stck.pop()
        if not visited[u]:
            visited[u] = True
            res.append(u)
            for v in reversed(graph[u]):
                if not visited[v]: stck.append(v)
    print(res)

graph = {}
n = (int(input("Enter the number of vertices: ")))
for i in range (n):
    edges = list(map(int, input(f"Enter neighbours of {i}: ").split()))
    graph[i] = edges

dfs(graph, n)