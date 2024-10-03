import heapq

# Setting a large negative value to represent infinity
INFINITY = float('inf')

def floyd_warshall(distances, vertices):
    next_vertices = [[None for _ in range(vertices)] for _ in range(vertices)]
    for i in range(vertices):
        next_vertices[i][i] = i
        for j in range(vertices):
            if distances[i][j] == 1:
                next_vertices[i][j] = j
    
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    next_vertices[i][j] = next_vertices[i][k]

    return next_vertices

# Sample graph data
graph = {}
num_vertices = int(input())
distances = [[INFINITY for _ in range(num_vertices)] for _ in range(num_vertices)]
packages = input().strip().split()
pkg_map = dict(enumerate(packages))
reverse_pkg_map = {pkg: idx for idx, pkg in pkg_map.items()}

for i in range(num_vertices):
    vertex_info = input().split()
    vertex_name = vertex_info[0]
    num_connections = int(vertex_info[1])
    graph[vertex_name] = []
    for _ in range(num_connections):
        connection = input()[7:].strip().split(', ')
        for conn in connection:
            distances[reverse_pkg_map[conn]][i] = 1

# Running Floyd-Warshall algorithm
next_vertices = floyd_warshall(distances, num_vertices)

# Finding the shortest cycle
shortest_cycle_length = INFINITY
for i in range(num_vertices):
    shortest_cycle_length = min(shortest_cycle_length, distances[i][i])

if shortest_cycle_length == INFINITY:
    print('SHIP IT')
else:
    for i in range(num_vertices):
        if distances[i][i] == shortest_cycle_length:
            start_vertex = i
            break
    cycle_path = [start_vertex]
    while len(cycle_path) != shortest_cycle_length:
        cycle_path.append(next_vertices[cycle_path[-1]][start_vertex])
    print(*map(lambda x: packages[x], cycle_path[::-1]))
