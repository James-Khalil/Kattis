import math


line = input().split()
options = int(line[0])
retire = int(line[1])
profits = 0
output = 10000000000
investments = []
#Find recouptimes for each
for _ in range(options):
    line = input().split()
    profit = int(line[0])
    cost = int(line[1])
    recoupTime = math.ceil(cost / profit)
    investments.append([recoupTime, profit, cost])
    


investments = sorted(investments, key=lambda x: x[0])
#Find shortest day requirement
#investments needs to be sorted by recoupTime (smallest recoup times first)
for investment in investments:
    if(investment[0] < output):      
        profits += investment[1]
        retire += investment[2]
    if(profits > 0):
        tempRetire = math.ceil((retire) / profits)
        if(tempRetire <= output or output == -1):
            output = tempRetire
print(output)