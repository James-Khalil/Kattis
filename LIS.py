
import bisect

def LIS(n):
    A = []
    line = input().split()
    for i in range(n):
        A.append(int(line[i]))

    k = 0
    lis_end = 0
    L = [0] * n
    L_id = [0] * n
    p = [-1] * n

    for i in range(n):
        pos = bisect.bisect_left(L, A[i], 0, k)
        L[pos] = A[i]  # greedifly overwrite this
        L_id[pos] = i  # remember the index too
        p[i] = L_id[pos - 1] if pos > 0 else -1  # predecessor info
        if pos == k:  # can extend LIS?
            k = pos + 1  # k = longer LIS by +1
            lis_end = i  # keep best ending i

    longest_substring_indices = []
    curr_index = lis_end
    while curr_index != -1:
        longest_substring_indices.append(curr_index)
        curr_index = p[curr_index]

    # Reverse the list to get the correct order
    longest_substring_indices.reverse()
    
    
    print(k)
    print(' '.join(map(str, longest_substring_indices)))

try:
    while True:
        n = int(input())  # Read input line by line
        LIS(n)
except:
    i = 1
