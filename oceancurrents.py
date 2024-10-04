import heapq

def dijkstra(graph, start_row, start_col, rows, cols, end_row, end_col):

    def get_neighbors(row, col):
        directions = [
            (-1, 0),  
            (-1, 1),  
            (0, 1), 
            (1, 1), 
            (1, 0),  
            (1, -1),  
            (0, -1),  
            (-1, -1)  
        ]
        neighbors = []
        for i, (dx, dy) in enumerate(directions):
            nx, ny = row + dx, col + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if i != int(graph[row][col]):
                    weight = 1
                else: 
                    weight = 0
                neighbors.append((nx, ny, weight))
        return neighbors
    
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start_row][start_col] = 0
    
    pq = [(0, start_row, start_col)]
    
    while pq:
        energy, row, col = heapq.heappop(pq)
        if energy > distances[row][col]:
            continue
        if row == end_row and col == end_col:
            return distances[row][col]
        for neighbor_row, neighbor_col, weight in get_neighbors(row, col):
            new_dist = energy + weight
            if new_dist < distances[neighbor_row][neighbor_col]:
                distances[neighbor_row][neighbor_col] = new_dist
                heapq.heappush(pq, (new_dist, neighbor_row, neighbor_col))
    
    return distances[end_row][end_col]

w, h = map(int, input().split())
graph = []
for i in range(h):
    graph.append(input())
    
cases = int(input())

for i in range(cases):
    rs, cs, rd, cd = map(int, input().split())
    rs -= 1
    cs -= 1
    rd -= 1
    cd -= 1
    cost = dijkstra(graph, rs, cs, w, h, rd, cd)
    print(cost)
