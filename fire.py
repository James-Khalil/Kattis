from collections import deque

def bfs(djikstra, queue1, queue2, fire):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue1:
        currx, curry = queue1.popleft()
        for dx, dy in directions:
            nextx, nexty = currx + dx, curry + dy
            if fire:
                if 1 <= nextx <= n and 1 <= nexty <= m and (djikstra[nextx][nexty] == '.' or djikstra[nextx][nexty] == '@'):
                    djikstra[nextx][nexty] = '*'
                    queue2.append((nextx, nexty))
            elif 0 <= nextx <= n+1 and 0 <= nexty <= m+1 and djikstra[nextx][nexty] == '.':
                djikstra[nextx][nexty] = '@'
                queue2.append((nextx, nexty))

cases = int(input())
for _ in range(cases):
    m, n = map(int, input().split())

    djikstra = [['.' for _ in range(m+2)] for _ in range(n+2)]

    for i in range(1, n+1):
        row = input().strip()
        for j in range(1, m+1):
            djikstra[i][j] = row[j-1]

    guys = [(i, j) for i in range(n+2) for j in range(m+2) if djikstra[i][j] == '@']
    fire = [(i, j) for i in range(n+2) for j in range(m+2) if djikstra[i][j] == '*']

    time = 0
    works = False
    while fire or guys:
        temp = []
        newfire = []

        bfs(djikstra, deque(guys), temp, False)
        bfs(djikstra, deque(fire), newfire, True)

        if any(djikstra[i][0] == '@' or djikstra[i][m+1] == '@' for i in range(n+2)) or any(djikstra[0][j] == '@' or djikstra[n+1][j] == '@' for j in range(m+2)):
            works = True

        guys = [(i, j) for i, j in temp if djikstra[i][j] != '*']
        fire = newfire
        time += 1

        if works:
            break

    if works:
        print(time)
    else:
        print("IMPOSSIBLE")
