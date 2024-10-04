#i mightve remembered there was a ted ed for this problem
#we're just gonna make a lookup
#(32*32 to make the lookup, binary search on list of size 32)
#This should run instantly
import bisect
elookup = [[1]]
for i in range(1,32):
    elookup[0].append(i + 1)
for i in range(1, 32):
    elookup.append([])
    for j in range(32):
        if(i > j):
            elookup[i].append(elookup[i-1][j])
        else:
            #The value at i is the value before it plus the egg before it plus 1
            elookup[i].append(elookup[i][j-1] + elookup[i-1][j-1] + 1)

n = int(input())
for _ in range(n):
    case = input().split()
    floors = int(case[0])
    eggs = int(case[1])
    temp = bisect.bisect_left(elookup[eggs - 1], floors) + 1
    if(temp > 32): print("Impossible")
    else: print(temp)
            