#Change to a BFS instead of a DFS. Then we can do DP
#If not, consider trying A*

def jump(start, length, cost):
    global totalmin
    if(cost >= totalmin):
        return
    if((start,length) in costMap and costMap[(start, length)] <= cost):
        return
    forwards = start + length + 1
    backwards = start - length
    if(forwards == n - 1):
        if(cost + squares[n - 1] < totalmin): 
            totalmin = cost + squares[n - 1]
        return
    if(forwards in squares):
        jump(forwards, length + 1, cost + squares[forwards])
    if(backwards in squares and backwards != start):
        jump(backwards, length, cost + squares[backwards])

n = int(input())
totalmin = 5000000
squares = {}
costMap = {}
for _ in range(n):
    squares[_] = int(input())
jump(0, 0, 0)
print(totalmin)
