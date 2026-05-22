import heapq
def dijkstra(graph, start):
    distances = {}
    for node in graph:
        distances[node] = float('inf')
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()
    print("\nInitial Routing Table\n------------------------------------------------")
    for node in distances:
        print(f"Router {node} --> {distances[node]}")
    while priority_queue:
        current_distance, current_router = heapq.heappop(priority_queue)
        if current_router in visited:
            continue
        visited.add(current_router)
        print(f"\nProcessing Router {current_router}\n------------------------------------------------")
        for neighbor, weight in graph[current_router]:
            print(f"Checking Path:\n{current_router} --> {neighbor}\nLink Cost = {weight}")
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                old_distance = distances[neighbor]
                distances[neighbor] = new_distance
                print(f"Updating Router {neighbor}\tOld Distance = {old_distance}\tNew Distance = {new_distance}")
                heapq.heappush(priority_queue,(new_distance, neighbor))
            else:
                print("No Update Required")
            print()
        print("Routing Table After Processing\n------------------------------------------------")
        for node in distances:
            print(f"Router {node} --> {distances[node]}")

    print("\nFinal Shortest Path Table\n------------------------------------------------\nDestination Router\tShortest Distance")
    for node in distances:
        print(f"{node}\t\t\t{distances[node]}")

graph = {}
n = int(input("Enter number of routers(vertices): "))
for i in range(n):
    neighbours = int(input(f"\nEnter number of neighbours for Router {i}: "))
    graph[i] = []
    for j in range(neighbours):
        neighbor, cost = map(int,
        input(f"Enter neighbour and cost for Router {i}: ").split())
        graph[i].append((neighbor, cost))
start = int(input("\nEnter starting router: "))
dijkstra(graph, start)