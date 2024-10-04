import bisect
import sys
from sortedcontainers import SortedDict, SortedSet
# Create a SortedSet
sorted_set = SortedSet()
N = int(input())
#input_lines = sys.stdin.read().splitlines()
for _ in range(N):
    command = input().split()
    if command[0] == 'add':
        energy, gold = map(int, command[1:])
        sorted_set.add((energy,gold))
        
    elif command[0] == 'query':
        energy = int(command[1])
        totalgold = 0
        while(energy > 0):
            index = bisect.bisect_right(sorted_set, (energy+1,-1))-1
            if(index == -1):
                break
            e,g = sorted_set.pop(index)
            totalgold += g
            energy -= e
            
        print(totalgold)