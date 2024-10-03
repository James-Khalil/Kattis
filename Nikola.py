from heapq import heappush, heappop

def jump(start, length, cost):
    global totalmin
    pq = [(cost, start, length)]  # Initialize priority queue with initial state
    while pq:
        cost, start, length = heappop(pq)  # Dequeue the state with the lowest cost
        if (start, length) in costMap and costMap[(start, length)] <= cost:
            continue
        costMap[(start, length)] = cost
        if cost >= totalmin:
            continue
        forwards = start + length + 1
        backwards = start - length
        if forwards == n - 1:
            totalmin = min(totalmin, cost + squares[n - 1])
            continue
        if forwards in squares:
            heappush(pq, (cost + squares[forwards], forwards, length + 1))
        if backwards in squares and backwards != start:
            heappush(pq, (cost + squares[backwards], backwards, length))

n = int(input())
totalmin = 5000000
squares = {}
costMap = {}
for _ in range(n):
    squares[_] = int(input())

jump(0, 0, 0)
print(totalmin)
