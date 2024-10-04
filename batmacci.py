n,m = map(int, input().split())

fibcount = [1,1]

for i in range(2,n):
    fibcount.append(fibcount[i-2] + fibcount[i-1])


def fib(n,m):
    while(n > 2):
        if m > fibcount[(n-2)-1]: #This means we look at second string
            n = n-1
            m = m-fibcount[(n-2)]
        else: 
            n = n-2

    if n == 2:
        return "A"
    if n == 1:
        return "N"


result = fib(n,m)
print(result)