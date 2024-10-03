def tridegen(sortedlist):
    for i in range(len(sortedlist)-2):
        a = sortedList[i]
        b = sortedList[i+1]
        c = sortedList[i+2]
        if a + b > c and b + c > a and a + c > b:
            return True
    return False


n,q = map(int,input().split())
trees = [[]] * n
for i in range(n):
    x,y,h = map(int,input().split())
    if trees[x]:
        trees[x].append((y,h))
    else:
        trees[x] = [(y,h)]

for i in range(q):
    sortedList = set()
    #Find all triangles that fit in the given area
    #Sort list (after checking it's greater than 3)
    #Send it over to tridegen
    xLow,yLow,xHigh,yHigh = map(int,input().split())
    for i in range(xLow, xHigh+1):
        for tree in trees[i]:
            if(yLow <= tree[0] and tree[0] <= yHigh and tree[1] not in sortedList):
                sortedList.add(tree[1])
    if(len(sortedList) < 3):
        print(0)
        continue
    sortedList = sorted(sortedList)
    if tridegen(sortedList): print(1)
    else: print(0)