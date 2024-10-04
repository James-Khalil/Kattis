
import sys
import heapq

def Quickscope():
    dict = {0:{}}
    n = int(input())
    library = {}
    nesting = 0 
    input_lines = sys.stdin.read().splitlines()

    for line in input_lines:
        line = line.split()
        #Typeof instance
        if(line[0] == "TYPEOF"):
            value = getLastValue(library, line[1])
            if(value != None):
                print(dict[value][line[1]])
            else:
                print("UNDECLARED")
        #Declaration instance       
        elif(line[0] == "DECLARE"):
            if(line[1] in dict[nesting]):
                print("MULTIPLE DECLARATION")
                return
            dict[nesting][line[1]] = line[2]
            if line[1] in library:
                # Key exists, append value to existing list
                library[line[1]].append(nesting)
            else:
                # Key does not exist, create new list with value
                library[line[1]] = [nesting]
        #Nesting block    
        elif(line[0] == "{"):
            nesting += 1
            dict[nesting] = {}
        #Nesting block
        elif(line[0] == "}"):
            removeNesting(library, dict[nesting].keys())
            nesting -= 1
           
def removeNesting(dictionary, hashset):
        for key in hashset:
            if key in dictionary:
                dictionary[key].pop()     
                
def getLastValue(library, key):
    if key in library and library[key]:
        return library[key][-1]
    else:
        return None  # Key not found or list is empty
    
    
Quickscope()