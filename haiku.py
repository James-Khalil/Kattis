from itertools import product

def options(word, syllable, memo):
    if (word, syllable) in memo:
        return memo[(word, syllable)]
    
    temp = ""
    combo = set()
    for i in range(len(word)):
        temp += word[i]
        if temp in syllables:
            combo |= set(options(word[i+1:], syllable+1, memo))
    if temp == "":
        combo.add(syllable)
    memo[(word, syllable)] = combo
    return combo

syllables = set()

def isHaiku(line, count, memo):
    comboList = [options(word, 0, memo) for word in line]
    
    for combination in product(*comboList):
        if sum(combination) == count:
            return True
    return False

n = int(input())

for _ in range(n):
    syllables.add(input())

line1 = input().split()
line2 = input().split()
line3 = input().split()

memo = {}  # Memoization dictionary
if isHaiku(line1, 5, memo) and isHaiku(line2, 7, memo) and isHaiku(line3, 5, memo):
    print("haiku")
else:
    print("come back next year")
