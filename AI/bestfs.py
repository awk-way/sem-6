from heapq import heappush, heappop

def best_first_search(graph, start, goal, heuristic):
    open_list, closed_list = [], set()
    heappush(open_list, (heuristic[start], start))
    parent = {start: None}

    while open_list:
        h, current = heappop(open_list)
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        closed_list.add(current)
        for neighbour in graph[current]:
            if neighbour not in closed_list:
                if neighbour not in parent:  
                    parent[neighbour] = current
                heappush(open_list, (heuristic[neighbour], neighbour))

    return None

graph, heuristic = {}, {}
n = int(input("Enter number of vertices: "))
for i in range(1, n+1):
    neighbours = list(map(int, input(f"Enter neighbours of {i}: ").split()))
    h_val = int(input(f"Enter heuristic value of {i}: "))
    graph[i] = neighbours
    heuristic[i] = h_val
start = int(input("\nEnter start node: "))
goal = int(input("Enter goal node: "))
path = best_first_search(graph, start, goal, heuristic)

print("\nPath found:", path)