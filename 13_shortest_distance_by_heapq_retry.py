import heapq

INF = int(1e9)
V, E = map(int, input().split())
K = int(input())-1
graph = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u-1].append((w, v-1))

d = [INF for _ in range(V)]
d[K] = 0
queue = []
heapq.heappush(queue, (d[K],K))

while queue:
    cur_d, cur_v = heapq.heappop(queue)
    if cur_d > d[cur_v]:
        continue
    for next_d, next_v in graph[cur_v]:
        if(d[next_v]>cur_d+next_d):
            d[next_v] = cur_d+next_d
            heapq.heappush(queue, (d[next_v], next_v))
            
for i in d:
	if i==INF:
		print("INF")
	else: 
		print(i)
    
