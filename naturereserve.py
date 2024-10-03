import heapq

def findRoot(unionFind, A):
    if unionFind[A] != A:
        unionFind[A] = findRoot(unionFind, unionFind[A])
    return unionFind[A]

def unionByRank(unionFind, rank, rootA, rootB):
    if rank[rootA] < rank[rootB]:
        unionFind[rootA] = rootB
        rank[rootB] = rootA
    else:
        unionFind[rootB] = rootA
        rank[rootA] = rootB

def kruskals(edges, n, initialStations):
    totalDistance = 0
    unionFind = [i for i in range(n)]
    rank = [0] * n
    edge_count = 0
    initial = initialStations.pop() - 1
    while initialStations:
        unionFind[initialStations.pop() - 1] = initial
        rank[initial] += 1
    while edges:
        dist, i, j = heapq.heappop(edges)
        rootA = findRoot(unionFind, i)
        rootB = findRoot(unionFind, j)
        if rootA != rootB:
            unionByRank(unionFind, rank, rootA, rootB)
            totalDistance += dist
            edge_count += 1
            if edge_count == n - 1:
                break
    return totalDistance

testcases = int(input())

for _ in range(testcases):
    n, m, l, s = map(int, input().split())
    initialStations = set(map(int, input().split()))
    edges = []
    for i in range(m):
        i,j,weight = map(int,input().split())
        heapq.heappush(edges, (weight, i-1, j-1))  # Push the edge into the priority queue
    activationCost = kruskals(edges, n, initialStations)
    programSendCost = l * (n - s)
    print(activationCost + programSendCost)
