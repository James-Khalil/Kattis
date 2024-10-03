import math

cases = int(input())

for _ in range(cases):
    a,b,d = map(int,input().split())
    gcd = math.gcd(a,b)
    if d % gcd == 0:
        print("Yes")
    else:
        print("No")
    