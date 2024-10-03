#I tried so hard to not use Tarjan's
#I could not do it

def find(adj, bridges, vis, par, hi, lo, curr):
    global dfstime
    vis[curr] = True
    hi[curr] = lo[curr] = dfstime
    dfstime += 1
    for next_node in adj[curr]:
        if not vis[next_node]:
            par[next_node] = curr
            find(adj, bridges, vis, par, hi, lo, next_node)
            lo[curr] = min(lo[curr], lo[next_node])
            if lo[next_node] > hi[curr]:
                bridges.append((next_node, curr))
        elif next_node != par[curr]:
            lo[curr] = min(lo[curr], hi[next_node])


def dfs(adj, vis, skip, curr):
    vis[curr] = True
    total = 1
    for next_node in adj[curr]:
        if vis[next_node]:
            continue
        if (curr, next_node) in skip or (next_node, curr) in skip:
            continue
        total += dfs(adj, vis, skip, next_node)
    return total


n, m = map(int, input().split())

# Read in graph
adj = [[] for _ in range(n)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)

bridges = []
vis = [False] * n
par = [-1] * n
hi = [-1] * n
lo = [-1] * n

dfstime = 0
find(adj, bridges, vis, par, hi, lo, 0)

skip = set(bridges)

vis = [False] * n

print(dfs(adj, vis, skip, 0))
