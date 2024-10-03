syllables = set()

def findCombinations(word,result):
    options = []
    temp = ""
    for i in range(len(word)):
        temp += word[i]
        if (temp in syllables):
            options.append(findCombinations(word[i:], result + 1))
    options.append(result)
    return options

def DPFind(combinations, goalnumber, current):
    if not combinations:
        if current == goalnumber:
            return True
        return False
    if current >= goalnumber: return False
    removedlist = combinations.pop(0)
    for number in removedlist:
        if current + number == goalnumber:
            return True
        elif current + number < goalnumber:
            if(DPFind(combinations, goalnumber,current+goalnumber)):
                return True
    return False

def findSyllables(line, goalnumber):
    #Option 1: We split as we go, dividing however we can
    #that didnt work, so we move onto
    #option 2: DP. At any junction that allows us to make a new syllable, we go ahead and do that, while also developing a path where we didn't make it a new syllable
    #Resulting in several branching paths, where only one has to result in the right answer.
    #If we brute force this it will likely be too slow, so instead we still gain all possible orientations, and perform a dp on that
    combinations = []
    for word in line:
        options = findCombinations(word,0)
        combinations.append(options)
    return DPFind(combinations, goalnumber, 0)


n = int(input())
for i in range(n):
    syllables.add(input())

line1 = input().split()
line2 = input().split()
line3 = input().split()

if(findSyllables(line1, 5) and findSyllables(line2,7) and findSyllables(line3,5)):
    print("haiku")
else:
    print("come back next year")