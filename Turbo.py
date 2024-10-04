def fenwick_subtract(tree, i):
    while i <= tree['size']:
        tree['sums'][i] -= 1
        i += i & -i

def fenwick_add(tree, i):
    while i <= tree['size']:
        tree['sums'][i] += 1
        i += i & -i

def fenwick_sum(tree, to):
    s = 0
    while to > 0:
        s += tree['sums'][to]
        to -= to & -to
    return s

def fenwick_init(tree, size):
    tree['sums'] = [0] * (size + 1)
    for i in range(1, size + 1):
        tree['sums'][i] = i & -i
    tree['size'] = size

def find_swaps_needed(n, fenwick, index):
    top = n >> 1
    for i in range(1, top + 1):
        left = i
        leftIndex = index[left]
        print(fenwick_sum(fenwick, leftIndex) - i)
        fenwick_add(fenwick, 1)
        fenwick_subtract(fenwick, leftIndex)

        right = n + 1 - i
        rightIndex = index[right]
        print(n - fenwick_sum(fenwick, rightIndex) - i + 1)
        fenwick_subtract(fenwick, rightIndex)

    if n & 1:
        print("0")

n = int(input())

fenwick = {}
fenwick_init(fenwick, n)

index = [0] * (n + 1)
for i in range(1, n + 1):
    tmp = int(input())
    index[tmp] = i

find_swaps_needed(n, fenwick, index)
