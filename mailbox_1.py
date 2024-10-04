
MAX_VALUE = 10**9
memo = [[[-1 for _ in range(101)] for _ in range(101)] for _ in range(11)]

def mail(k, a, m):
    if k == 1:
        return (m * (m + 1)) // 2 - (a * (a + 1)) // 2
    if a == m:
        return 0

    if memo[k][a][m] == -1:
        res = MAX_VALUE
        for i in range(a + 1, m + 1):
            res = min(res, i + max(mail(k - 1, a, i - 1), mail(k, i, m)))
        memo[k][a][m] = res
    return memo[k][a][m]

n = int(input())
for _ in range(n):
    k, m = map(int, input().split())
    print(mail(k, 0, m))
