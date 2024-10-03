
straightaways, lanes = map(int, input().split())
laneLength, changeLength = map(int, input().split())
sections = []

#This is a list detailing the minimum for a given lane
#It will contain n items, where n is the number of lanes
minLane = [None] * (lanes + 1)
tempLane = [None] * (lanes + 1)

#Tuple explanation
#[0] is the length of the straightaway
#[1] is the stretch of the curve
#[2] is the curvature of the curve

firstlane = int(input())
shifted = 0
while firstlane >= 0 and 1 + shifted <= lanes:
    minLane[1 + shifted] = firstlane + (changeLength + laneLength) * shifted
    shifted += 1
    firstlane -= laneLength

for i in range(straightaways - 1):
    sections.append([int(input()),0,0])

for i in range(straightaways - 1):
    curves = input().split()
    sections[i][1] = int(curves[0])
    sections[i][2] = int(curves[1])



for section in sections:
    #Calcualte the curve
    for i in range(1, len(minLane)):
        if minLane[i] is None: break
        minLane[i] += section[1] + i * section[2] + section[0]
    #Simulate the lane changes to see if anything improves
    tempLane = minLane.copy()
    for i in range(1, len(minLane)):
        if minLane[i] is None: break
        shifted = 0
        length = section[0]
        #Check all lanes to the right
        while length >= 0 and i + shifted <= lanes:
            #Possible is the minimum distance for shifting over from i
            #So we take away it travelling straight and add what if it travelled in a different pattern
            possible = (minLane[i] - section[0]) + length + (changeLength + laneLength) * shifted
            if(not minLane[i + shifted]):
                tempLane[i + shifted] = possible
            else: 
                tempLane[i + shifted] = min(tempLane[i + shifted], possible)
            shifted += 1
            length -= laneLength
        
        shifted = 0
        length = section[0]
        #Check all lanes to the left
        while length >= 0 and i + shifted > 0:
            possible = (minLane[i] - section[0]) + length + (changeLength + laneLength) * abs(shifted)
            if(not minLane[i + shifted]):
                tempLane[i + shifted] = possible
            else: 
                tempLane[i + shifted] = min(tempLane[i + shifted], possible)
            shifted -= 1
            length -= laneLength
    minLane = tempLane.copy()
print(minLane[1])