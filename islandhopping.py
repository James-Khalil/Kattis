testcases = int(input())

for _ in range(testcases):
    islands = int(input)
    endpoints = []
    edges = []
    for i in range(islands):
        x,y = map(int, input().split())
        endpoints.append((x,y))
    #Create the edges
    
    edges.sort()
    
    #Perform kruskals