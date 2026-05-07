import heapq

def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    g_cost = {node: float('inf') for node in graph}
    g_cost[start], parent, closed_list = 0, {start: None}, set()

    while open_list:
        current_f, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1], g_cost[goal]

        closed_list.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor in closed_list:
                continue
            tentative_g = g_cost[current] + cost

            if tentative_g < g_cost[neighbor]:
                parent[neighbor] = current
                g_cost[neighbor] = tentative_g
                f = tentative_g + heuristic[neighbor]
                heapq.heappush(open_list, (f, neighbor))

    return None, float('inf')

graph, heuristic = {}, {}
n = int(input("Enter number of vertices: "))

for i in range(1, n+1):
    graph[i] = {}
    num_neighbors = int(input(f"\nEnter number of neighbors of {i}: "))
    for _ in range(num_neighbors):
        neighbor, cost = map(int, input("Enter neighbor and cost: ").split())
        graph[i][neighbor] = cost
    h_val = int(input(f"Enter heuristic value of {i}: "))
    heuristic[i] = h_val

start = int(input("\nEnter start node: "))
goal = int(input("Enter goal node: "))
path, cost = a_star(start, goal)
print (f"\nOptimal Path:{path}    Total Cost: {cost}")