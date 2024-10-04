# Function to parse the input line and update data accordingly
from collections import defaultdict
import sys

def main():
    line = input()
    time = 0
    correct = 0
    hashmap = defaultdict(int)
    while(line != "-1"):
        #0 = time, 1 = letter, 2 = right/wrong
        parsed = line.split()
        if(parsed[2] == "right"):
            correct += 1
            time += int(parsed[0])
            time += hashmap[parsed[1]]
        else:
            hashmap[parsed[1]] += 20
        line = input()
    print(str(correct) + " " + str(time))

def space():
    depth = -1
    tvalue = 0
    space = 0
    initialS = 0
    intialT = 0
    hashmap = defaultdict(int)
    n = int(input())  # Read the first line

    for _ in range(n):
        line = input()
        sCount = line.count('s')
        tCount = line.count('t')
        if '{' in line:
            depth += 1
        if depth in hashmap:
            if((tCount == 0) & (sCount != 0)):
                if(sCount % depth != 0):
                    print(-1)
                    return
                if((space == 0)):
                    space = int(sCount / depth)
                elif((int(sCount / depth) != space)):
                    print(-1)
                    return
            sDiff = sCount - hashmap[depth][0]
            tDiff = tCount - hashmap[depth][1]
            if(((tDiff == 0) & (sDiff != 0)) | ((tDiff != 0) & (sDiff == 0)) | (sDiff * tDiff > 0)):
                print(-1)
                return
            if((tDiff != 0) & (sDiff != 0)):
                tempT = int(abs(sDiff / tDiff))
                if ((sDiff % tDiff != 0) | ((tvalue != 0) & (tvalue != tempT))):
                    print(-1)
                    return
                tvalue = tempT
                if((sCount + tCount * tvalue) % depth != 0):
                    print(-1)
                    return
                if(space == 0):
                    space = int((sCount + tCount * tvalue) / depth)
                elif((space != int((sCount + tCount * tvalue) / depth))):
                    print(-1)
                    return
        else:
            if(depth != 0):
                if(tCount == 0):
                    if(sCount % depth != 0):
                        print(-1)
                        return
                elif(((sCount + tCount * tvalue) % depth != 0) & tvalue != 0):
                    print(-1)
                    return            
            hashmap[depth] = (sCount, tCount)
        if '}' in line:
            depth -= 1
    if(tvalue == 0):
        tvalue = 1
    print(tvalue)
    
def equalizer():
    n = int(input())
    swaps = 0
    convert0 = 0
    for _ in range(n):
        S = input()
        T = input()
        #If different lengths or S has more 1s then T it's impossible
        if((len(S) != len(T)) | (S.count('1') > T.count('1'))):
            print("Case " + str(_ + 1) + ": -1")
            continue
        
        #Number of ones we need to convert for but subtract ? because if ? is there we must convert to 1 before 0
        qCount = S.count('?')
        diff0 = (T.count('1') - S.count('1')) - S.count('?')
        diffQ = min(T.count('1') - S.count('1'), qCount)
        if(diff0 > 0):
            convert0 = diff0
        
        for i in range(len(S)):
            #If we have a 1 facing a 0 we must swap
            if(T[i] == '0') & (S[i] == '1'):
                swaps += 1      
            #Handles when we have a 0 that could either swap or convert
            if((T[i] == '1') & (S[i] == '0')):
                if(diff0 > 0):
                    diff0 -= 1
                else:
                    swaps += 1
            #With ?, we avoid swap whenever possible. Only two situations where swap must happen
            #We have a 0 but we need to convert to 1
            #We have a 1 but we need to convert to 0
            if(S[i] == '?'):
                if(T[i] == '1'):
                    if(diffQ <= 0):
                        swaps += 1
                    else:
                        diffQ -= 1
                elif((T[i] == '0') & (diffQ == qCount)):
                    swaps+= 1
                    diffQ -= 1
                qCount -= 1
        print("Case " + str(_ + 1) + ": " + str(int(swaps/2 + S.count('?') + convert0)))
        swaps = 0
        convert0 = 0


def Biased():
    n = int(input())
    for _ in range(n):
        sum = 0
        array = []
        input()
        i = int(input())
        for _ in range(i):
            array.append(int(input().split()[1]))
        array.sort()
        for _ in range(i):
            sum += abs((_ + 1) - array[_])
        print(sum)

def Quickscope():
    dict = {0:{}}
    n = int(input())
    nesting = 0 
    for _ in range(n):
        line = input().split()
        #Typeof instance
        if(line[0] == "TYPEOF"):
            if(line[1] in dict[nesting]):
                print(dict[nesting][line[1]])
            else:
                print("UNDECLARED")
         #Declaration instance       
        elif(line[0] == "DECLARE"):
            if(line[1] in dict[nesting]):
                print("MULTIPLE DECLARATION")
                return
            dict[nesting][line[1]] = line[2]
        #Nesting block    
        elif(line[0] == "{"):
            nesting += 1
        #Nesting block
        elif(line[0] == "}"):
            nesting -= 1
            
Quickscope()