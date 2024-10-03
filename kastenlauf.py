import math
from collections import deque

def drManhattan(x1, y1, x2, y2):
    return 1000 >= abs(x1 - x2) + abs(y1 - y2)

def canReach(joX, joY, bergX, bergY, stores):
    queue = deque([(joX, joY)])
    while queue:
        x, y = queue.popleft()
        if drManhattan(x, y, bergX, bergY):
            return True
        for i in range(len(stores) - 1, -1, -1):
            storeX, storeY = stores[i]
            if drManhattan(x, y, storeX, storeY):
                queue.append((storeX, storeY))
                del stores[i]
        if drManhattan(x, y, bergX, bergY):
            return True
    return False

# Example usage:
testcases = int(input())
for _ in range(testcases):
    n = int(input())
    joX, joY = map(int, input().split())
    stores = []
    for i in range(n):
        x, y = map(int, input().split())
        stores.append((x, y))
    bergX, bergY = map(int, input().split())
    if canReach(joX, joY, bergX, bergY, stores):
        print("happy")
    else:
        print("sad")
