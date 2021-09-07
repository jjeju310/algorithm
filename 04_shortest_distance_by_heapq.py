import sys
import heapq

INF = int(1e9)

V, E = map(int, input().split())
start = int(input())-1

graph= [[] for _ in range(V)]

for _ in range(E):
	u, v, w = map(int, sys.stdin.readline().split())
	graph[u-1].append((w,v-1)) #(거리, 노드번호)
print (graph)

d = [INF for _ in range(V)] # 최소 거리 리스트
d[start] = 0 # 시작 노드 - 시작 노드의 거리는 0
queue = [] 
heapq.heappush(queue, (d[start],start)) # 시작 정점의 (거리, 노드번호)를 우선순위 큐에 삽입 

while queue: # 큐에 아무것도 없으면 종료
	cur_d, cur_node = heapq.heappop(queue) # 기준 정점이 되는 노드
	if d[cur_node] < cur_d: #시작점으로부터 현재 노드까지의 최소거리보다 기준 노드의 거리가 더 크면 이미 방문한 노드로 볼 수 있음
		continue

	for next_d, next_node in graph[cur_node]: #현재 노드와 인접한 노드의 (거리, 노드번호)
		new_d = cur_d + next_d # 현재노드까지의 최소 거리 + 인접한 노드와의 거리
		if d[next_node] > new_d: # 최소 거리보다 새로 구한 거리가 더 작으면
			d[next_node] = new_d # 최소 거리 값을 갱신
			heapq.heappush(queue, (d[next_node], next_node)) # 해당 인접 노드를 큐에 추가

for i in d:
	if i==INF:
		print("INF")
	else: 
		print(i)