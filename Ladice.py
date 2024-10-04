class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.empty = [1] * n

    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        
        # Path compression: Update parent pointers along the path to the root
        while self.parent[x] != root:
            x, self.parent[x] = self.parent[x], root
        
        return root

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        self.parent[root_y] = root_x

# Read input
first = input().split()
items = int(first[0])
drawers = int(first[1])
uf = UnionFind(drawers+1)
for _ in range(items):
    pair = input().split()
    A = int(pair[0])
    B = int(pair[1])
    rootA = uf.find(A)
    rootB = uf.find(B)
    if(uf.empty[rootA] > 0 or uf.empty[rootB] > 0):
        if(rootA != rootB):
            uf.empty[rootA] += uf.empty[rootB] -1
            uf.empty[rootB] += uf.empty[rootA] -1
        else:
            uf.empty[rootA] -= 1
        uf.union(A, B)
        print("LADICA") 
    else:
        print("SMECE")