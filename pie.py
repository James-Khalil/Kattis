import math


def craftablePies(area, pieAreaList):
    count = 0
    for pie in pieAreaList:
        count += pie//area

    return count

def pinarySearch(high, friends, pieAreaList):
    low = 0
    mid = 0
    topresult = 0
    while low <= high:
        if abs(mid - ((low + high) / 2)) <= 0.0001:
            return topresult
        mid = (low + high) / 2
        #if we can make enough pies for friends we need to increase the area and see if that still works
        if craftablePies(mid, pieAreaList) >= friends:
            topresult = mid
            low = mid
        #If we cant make enough pies for friends we need to shrink the area
        else:
            high = mid


n = int(input())
for i in range(n):
    tobeparsed = input().split()
    pies = int(tobeparsed[0])
    friends = int(tobeparsed[1]) + 1
    pielist = input().split()
    pieAreaList = []
    largestpie = 0
    for pie in pielist:
        area = math.pow(int(pie),2) * math.pi
        pieAreaList.append(area)
        largestpie = max(area, largestpie)

    print(pinarySearch(largestpie, friends, pieAreaList))

    
