#this is like the first thing they teach in 413
#i love greedy baby
n = int(input())
greedy = []
for _ in range(n):
    line = input().split()
    enter = int(line[0])
    exit = int(line[1])
    greedy.append([enter,exit])

#Sort by exit times
greedy.sort(key=lambda x: x[1])
count = 0
exit = 0
for interval in greedy:
    if(exit <= interval[0]):
        exit = interval[1]
        count += 1
print(count)