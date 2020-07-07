import collections

# returns topological ordering
def topologicalSorting(numCourses, prerequisites):
    edges=[0 for _ in range(numCourses)]
    graph=[set() for _ in range(numCourses)]
    result=[]
    for u,v in prerequisites:
        edges[u]+=1
        graph[v].add(u)
        
    queue=collections.deque([i for i,number in enumerate(edges) if number==0])
    while queue:
        node=queue.popleft()
        result.append(node)
        for edge in graph[node]:
            edges[edge]-=1
            if edges[edge]==0:
                queue.append(edge)
    for edge in edges:
        if edge>0:
            return []
    return result