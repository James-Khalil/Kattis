import math
import heapq

def squared_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def findRoot(unionFind, A):
    if unionFind[A] == A:
        return A
    unionFind[A] = findRoot(unionFind, unionFind[A])
    return unionFind[A]

def unionByRank(unionFind, rank, A, B):
    rootA = findRoot(unionFind, A)
    rootB = findRoot(unionFind, B)
    if rootA != rootB:
        if rank[rootA] < rank[rootB]:
            unionFind[rootA] = rootB
        elif rank[rootA] > rank[rootB]:
            unionFind[rootB] = rootA
        else:
            unionFind[rootB] = rootA
            rank[rootA] += 1

def kruskals(edges, n):
    totalDistance = 0
    unionFind = [i for i in range(n)]
    rank = [0] * n
    heapq.heapify(edges)  # Convert the list of edges into a priority queue
    edge_count = 0
    while edge_count < n - 1 and edges:
        dist, i, j = heapq.heappop(edges)  # Pop the edge with the smallest weight
        rootA = findRoot(unionFind, i)
        rootB = findRoot(unionFind, j)
        if rootA != rootB:
            unionByRank(unionFind, rank, rootA, rootB)
            totalDistance += dist
            edge_count += 1
    return totalDistance

testcases = int(input())

for _ in range(testcases):
    islands = int(input())
    endpoints = []
    edges = []
    for i in range(islands):
        x, y = map(float, input().split())
        endpoints.append((x, y))
    for i in range(len(endpoints)):
        for j in range(i + 1, len(endpoints)):
            dist = squared_euclidean_distance(endpoints[i], endpoints[j])
            heapq.heappush(edges, (dist, i, j))  # Push the edge into the priority queue

    # Perform Kruskal's
    print(kruskals(edges, islands))
