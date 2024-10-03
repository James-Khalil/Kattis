import heapq
#Big brain idea
#We are using a pq to keep track of where to go
def conquer_islands(graph, island_costs):
    pq = []
    total_army = island_costs[0]
    conquered = set()
    conquered.add(0)
    for visitable in graph[0]:
        heapq.heappush(pq, (island_costs[visitable], visitable))

    while pq:
        army, island = heapq.heappop(pq)
        if island in conquered:
            continue
        elif army < total_army:
            #If you conquer an island, you need to mark it conquered, and append all visitable islands onto our stack
            conquered.add(island)
            for visitable in graph[island]:
                if visitable not in conquered:
                    heapq.heappush(pq, (island_costs[visitable], visitable))
            total_army += island_costs[island]
        else:
            return total_army

    return total_army


islands, bridges = map(int, input().split())

graph = {i: [] for i in range(islands)} 
islandCosts = [0] * islands
for i in range(bridges):
    a,b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(islands):
    islandCosts[i] = int(input())
    
print(conquer_islands(graph, islandCosts))

    
#We need to efficiently check for islands we can go to
#We want to avoid going to islands more than once
#We could keep a list of islands available to us
#and use a binary heap to see which islands we can hit
#i think logn is the best