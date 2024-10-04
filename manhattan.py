#If we sort by the coordinates to ensure we don't moyCorde backwards (cause shortest path to work means only going towards work)
#Then we can find paths stemming from that
#I think treasure hunt in 413 also had a similar yCordiable algorithm but idk


def LIS(yCord):
    parent = [-1] * len(yCord)
    temp = [0] * len(yCord)
    
    lis = 1
    for i in range(1, len(yCord)):
        if yCord[i] <= yCord[temp[0]]:
            temp[0] = i
        elif yCord[i] > yCord[temp[lis - 1]]:
            parent[i] = temp[lis - 1]
            temp[lis] = i
            lis += 1
        else:
            l, r = -1, lis - 1
            while r - l > 1:
                m = l + (r - l) // 2
                if yCord[temp[m]] >= yCord[i]:
                    r = m
                else:
                    l = m
            parent[i] = temp[r - 1]
            temp[r] = i
    
    ans = []
    i = temp[lis - 1]
    while i >= 0:
        ans.append(i)
        i = parent[i]
    
    return ans[::-1]

n = int(input())
x1, y1, x2, y2 = map(int, input().split())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    if x > max(x1, x2) or x < min(x1, x2) or y > max(y1, y2) or y < min(y1, y2):
        continue
    points.append((x, y))

# Count real points, edge cases none
n = len(points)
if n == 0:
    print("0")
    exit()

# Sanitize points
currMinY = min(y1, y2)
for i in range(n):
    points[i] = (points[i][0], points[i][1] - currMinY)
y1 -= currMinY
y2 -= currMinY
if (y1 > y2) != (x1 > x2):
    y1, y2 = y2, y1
    for i in range(n):
        points[i] = (points[i][0], abs(y1 - y2) - points[i][1])

# Prepare LIS
points.sort()
yCord = [(point[1], i) for i, point in enumerate(points)]

print(len(LIS(yCord)))
