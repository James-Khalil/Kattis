first = input().split()
residents = int(first[0])
time = int(first[1])
barTimes = []
for _ in range(residents):
    line = input().split()
    enter = int(line[0])
    exit = int(line[1])
    barTimes.append([enter, 0])
    barTimes.append([exit, 1])
        
barTimes.sort(key=lambda x: x[0])
#calcualte how many people are in the bar at each time interval
#
currentTime = 0
currentFriends = 0
exitFriends = 0
maxFriends = 0
for barTime in barTimes:
    if(barTime[0] != currentTime):
        currentTime = barTime[0]
        maxFriends = max(currentFriends, maxFriends)
        currentFriends -= exitFriends
        exitFriends == 0
    if(barTime[1] == 0): currentFriends += 1
    else: exitFriends += 1
    
print(maxFriends)