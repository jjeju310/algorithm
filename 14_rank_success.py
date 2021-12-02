from collections import deque
def solution(n, results):
    answer = 0
    indegree = [0]*(n+1) #진입차수
    degree = [0]*(n+1) #진출차수
    sum_gree = [0]
    graph1 = [[] for i in range(n+1)]
    graph2 = [[] for i in range(n+1)]
    for e in results:
        graph1[e[0]].append(e[1])
        indegree[e[1]] += 1
    for e in results:
        graph2[e[1]].append(e[0])
        degree[e[0]] += 1
    print(graph1)
    print(indegree)
    print(graph2)
    print(degree)
    
    for i in range(1, len(indegree)):
        sum_gree.append(degree[i]+indegree[i])
    print(sum_gree)
    
    result = topology_sort(n, indegree, graph1)
    
    for d in degree:
        if (n-1) == d:
            answer += 1
    for d in indegree:
        if (n-1) == d:
            answer += 1
    
    for i, sd in enumerate(sum_gree):
        if ((n-1)==sd) and ((n-1)!=degree[i]) and ((n-1)!=indegree[i]):
            answer += 1
            rank = result.index(sd)
            
        
    return answer

def topology_sort(v, indegree, graph):
    result = [0]
    q = deque()
    for i in range(1, v+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end='')
        
    return result