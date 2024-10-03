import bisect


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return False


n, m, a, c, x = map(int, input().split())

sequence = []
end = (x*a + c) % m
sequence.append(end)
for number in range(n-1):
    xi = (end * a + c) % m
    end = xi
    sequence.append(end)

count = 0
for number in sequence:
    if(binary_search(sequence, number)):
        count += 1

print(count)