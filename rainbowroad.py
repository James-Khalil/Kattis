import heapq
#Node and edge design is copied (although only the basic stuff to get a start)
class Edge:
    def __init__(self, dest, weight, color):
        self.dest = dest
        self.weight = weight
        self.color = color

class State:
    def __init__(self, dist, subset, node):
        self.dist = dist
        self.subset = subset
        self.node = node

    def __lt__(self, other):
        if self.dist == other.dist:
            if self.subset == other.subset:
                return self.node < other.node
            return self.subset < other.subset
        return self.dist < other.dist

def get_bit(c):
    if c == 'R': return 1
    if c == 'O': return 2
    if c == 'Y': return 4
    if c == 'G': return 8
    if c == 'B': return 16
    if c == 'I': return 32
    if c == 'V': return 64
    return 0


n, m = map(int, input().split())

adj = [[] for _ in range(n)]

for _ in range(m):
    n1, n2, w, c = input().split()
    n1, n2, w = int(n1) - 1, int(n2) - 1, int(w)
    adj[n1].append(Edge(n2, w, get_bit(c)))
    adj[n2].append(Edge(n1, w, get_bit(c)))

dist = [[float('inf')] * n for _ in range(128)]

s = []
dist[0][0] = 0
heapq.heappush(s, State(0, 0, 0))

while s:
    curr = heapq.heappop(s)
    subset = curr.subset
    currA = curr.node

    # Check if the current state is already outdated
    if dist[subset][currA] < curr.dist:
        continue

    for i in adj[currA]:
        next_, weight, color = i.dest, i.weight, i.color
        nextset = subset | color

        if dist[nextset][next_] > dist[subset][currA] + weight:
            dist[nextset][next_] = dist[subset][currA] + weight
            heapq.heappush(s, State(dist[nextset][next_], nextset, next_))

print(dist[(128) - 1][0])
