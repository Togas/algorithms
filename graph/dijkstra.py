#input is tupel with 0=u, 1=v, 2=weight between u and v
def dijkstra(array):
    graph=[[] for _ in range(len(array))]
    for u,v,w in array:
        graph[u].append((v,w))
        graph[v].append((w,v))
    parent=[-1 for _ in range(len(array))]
    values=[float("inf") for _ in range(len(array))]
    values[0]=0
    visited=[False for _ in range(len(array))]
    current=0
    visited[0]=True
    nextElement=0
    nextElementW=float("inf")
    allVisited=False
    while not allVisited:
        allVisited=True
        for u,w in graph[current]:
            if u not in visited:
                allVisited=False
                values[u]=min(values[u], values[current] + w)
                if values[u]<nextElementW:
                    nextElement=u
                    nextElementW=values[u]
        parent[nextElement]=current
        current=nextElement
        visited[nextElement]=True

