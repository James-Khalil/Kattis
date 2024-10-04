import sys

class UnionFind:
    def __init__(self, n):
        self.sets = [{i} for i in range(n)]
        self.index = [i for i in range(n)]
        self.total = [i for i in range(n)]

    def find(self, x):
        return self.index[x]
    
    def move(self, x, y):
        xIndex = self.find(x)
        yIndex = self.find(y)
        if(xIndex != yIndex):
            self.sets[xIndex].discard(x)
            self.sets[yIndex].add(x)
            self.index[x] = self.index[y]
            self.total[yIndex] += x
            self.total[xIndex] -= x

    def union(self, x, y):
        xIndex = self.find(x)
        yIndex = self.find(y)
        if(xIndex != yIndex):
            if(len(self.sets[xIndex]) < len(self.sets[yIndex])):
                self.subUnion(x,y)
            else:
                self.subUnion(y,x)
                
    def subUnion(self, g, t):
        givingIndex = self.find(g)
        takingIndex = self.find(t)
        for each in self.sets[givingIndex]:
            self.index[each] = takingIndex
            self.sets[takingIndex].add(each)
            self.total[takingIndex] += each
            self.total[givingIndex] -= each
        self.sets[givingIndex].clear()
        
# Read input
for line in sys.stdin:
    first = line.strip().split()
    p = int(first[0])
    n = int(first[1])
    uf = UnionFind(p + 1)
    for _ in range(n):
        pair = sys.stdin.readline().strip().split()
        command = pair[0]
        if(command == "1"):
            uf.union(int(pair[1]), int(pair[2]))
        elif(command == "2"):
            uf.move(int(pair[1]), int(pair[2]))
        else:
            count = len(uf.sets[uf.index[int(pair[1])]])
            total = uf.total[uf.index[int(pair[1])]]
            print(count , total)
