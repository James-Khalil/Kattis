import bisect
def remove_values(dict):
    low = True
    small = 1
    big = len(dict)
    while dict:
        print(dict[small] - 1)
        del dict[small]

# Read input
N = int(input())
unsorted = {}
for _ in range(N):
    unsorted[int(input())] = _
    

remove_values(unsorted)