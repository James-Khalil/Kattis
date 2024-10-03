import heapq
from itertools import combinations

def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to store nodes to visit, ordered by distance
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if the node has already been visited
        if current_distance > distances[current_node]:
            continue

        # Visit neighbors and update distances
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def tsp_shortest_path(graph, start, target_nodes):
    # Compute pairwise shortest paths
    shortest_paths = {}
    for node in target_nodes:
        shortest_paths[node] = dijkstra(graph, node)

    # Dynamic programming to find the shortest path that visits all nodes
    dp = {}
    for node in target_nodes:
        if node == start:
            continue
        dp[(node,), node] = shortest_paths[start][node]

    for r in range(2, len(target_nodes) + 1):
        for subset in combinations(target_nodes, r):
            for node in target_nodes:
                if node in subset or node == start:
                    continue
                dp[subset, node] = min(dp.get((tuple(sorted(set(subset) - {node})), k), float('inf')) + shortest_paths[k][node] for k in subset if k != node)


    # Find the shortest path
    shortest_path = min(dp.get((tuple(target_nodes), node), float('inf')) + shortest_paths[node][start] for node in target_nodes if node != start)

    return shortest_path



n,m = map(int, input().split())
graph = {}
for a in range(1, n+1):  # Assuming you want keys from 1 to 7
    graph[a] = []
for i in range(m):
    a,b,w = map(int, input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))
start_node = 1
target_nodes = list(map(int, input().split()))
shortest_path = tsp_shortest_path(graph, start_node, target_nodes)
print("Shortest path to visit all nodes from node", start_node, ":", shortest_path)