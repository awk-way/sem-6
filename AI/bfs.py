from collections import deque

def bfs(graph, n):
    visited, res = [False] * n, []
    q = deque()
    
    s = 0
    q.append(s)
    visited[s] = True

    while q:
        u = q.popleft()
        res.append(u)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    print(res)

graph = {}
n = (int(input("Enter the number of vertices: ")))
for i in range (n):
    edges = list(map(int, input(f"Enter neighbours of {i}: ").split()))
    graph[i] = edges

bfs(graph, n)