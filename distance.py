import math

#X and Y are measured seperately so that's cool
#Sort the lists, then, instead of calcualting distance for each
#Calculate it once, then add distance as it increases
n = int(input())
streets = []
avenues = []
for i in range(n):
    s,a = map(int, input().split())
    streets.append(s)
    avenues.append(a)
distance = 0
streetDistance = 0
avenueDistance = 0
streets.sort()
avenues.sort()
for i in range(n):
    streetDistance += streets[i] - streets[0]
    avenueDistance += avenues[i] - avenues[0]
    
distance += streetDistance
distance += avenueDistance
for i in range(1, n):
    sChange = streets[i] - streets[i-1]
    streetDistance -= sChange * (n - i)
    
    aChange = avenues[i] - avenues[i-1]
    avenueDistance -= aChange * (n - i)
    
    distance += streetDistance
    distance += avenueDistance
    
print(distance)