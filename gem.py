#John please dont make fenwick trees on the next mini contest i will fail i only copy fenwick trees i never write them
class FenwickTree:
    def __init__(self, arr):
        self.size = len(arr)
        self.tree = [0] * (self.size + 1)

        # Initialize Fenwick tree based on the given array
        for i in range(1, self.size + 1):
            self.update(i, arr[i - 1])

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index  # Move to the next node with non-zero least significant bit

    def query(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index  # Move to the parent node
        return total

    def range_query(self, start, end):
        return self.query(end) - self.query(start - 1)  # Compute the range sum

n,q = map(int, input().split())
gemvalues = input().split()
gems = []
for gemvalue in gemvalues:
    gems.append(int(gemvalue))
gemstring = input()
a1 = [0] * n
a2 = [0] * n
a3 = [0] * n
a4 = [0] * n
a5 = [0] * n
a6 = [0] * n

for i in range(len(gemstring)):
    if(int(gemstring[i]) == 1):
        a1[i] = 1
    elif(int(gemstring[i]) == 2):
        a2[i] = 1
    elif(int(gemstring[i]) == 3):
        a3[i] = 1
    elif(int(gemstring[i]) == 4):
        a4[i] = 1
    elif(int(gemstring[i]) == 5):
        a5[i] = 1
    elif(int(gemstring[i]) == 6):
        a6[i] = 1
        

fenwick1 = FenwickTree(a1)
fenwick2 = FenwickTree(a2)
fenwick3 = FenwickTree(a3)
fenwick4 = FenwickTree(a4)
fenwick5 = FenwickTree(a5)
fenwick6 = FenwickTree(a6)

for i in range(q):
    line = input().split()
    query = line[0]
    
    if query == "1":
        gemIndex = int(line[1])
        newGem = int(line[2])
        if a1[gemIndex-1] == 1:
            a1[gemIndex-1] = 0
            fenwick1.update(gemIndex, -1)
        elif a2[gemIndex-1] == 1:
            a2[gemIndex-1] = 0
            fenwick2.update(gemIndex, -1)
        elif a3[gemIndex-1] == 1:
            a3[gemIndex-1] = 0
            fenwick3.update(gemIndex, -1)
        elif a4[gemIndex-1] == 1:
            a4[gemIndex-1] = 0
            fenwick4.update(gemIndex, -1)
        elif a5[gemIndex-1] == 1:
            a5[gemIndex-1] = 0
            fenwick5.update(gemIndex, -1)
        elif a6[gemIndex-1] == 1:
            a6[gemIndex-1] = 0
            fenwick6.update(gemIndex, -1)
        
        if newGem == 1:
            a1[gemIndex-1] = 1
            fenwick1.update(gemIndex, 1)
        elif newGem == 2:
            a2[gemIndex-1] = 1
            fenwick2.update(gemIndex, 1)
        elif newGem == 3:
            a3[gemIndex-1] = 1
            fenwick3.update(gemIndex, 1)
        elif newGem == 4:
            a4[gemIndex-1] = 1
            fenwick4.update(gemIndex, 1)
        elif newGem == 5:
            a5[gemIndex-1] = 1
            fenwick5.update(gemIndex, 1)
        elif newGem == 6:    
            a6[gemIndex-1] = 1
            fenwick6.update(gemIndex, 1)
    elif query == "2":
        gem = int(line[1])
        newVal = int(line[2])
        gems[gem-1] = newVal
    else:
        startI = int(line[1])
        endI = int(line[2])
        total = 0
        total += fenwick1.range_query(startI,endI) * gems[0]
        total += fenwick2.range_query(startI,endI) * gems[1]
        total += fenwick3.range_query(startI,endI) * gems[2]
        total += fenwick4.range_query(startI,endI) * gems[3]
        total += fenwick5.range_query(startI,endI) * gems[4]
        total += fenwick6.range_query(startI,endI) * gems[5]
        print(total)