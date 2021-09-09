import heapq
INF = int(1e9)
distance = [INF] * (v+1)
input = stdin.readline
v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph} 
    # 1. 시작정점 start부터 N정점까지의 거리를 담는 배열. 시작 정점 자신을 제외한 모든 정점까지의 거리를 무한대로 초기화한다.
    distances[start] = 0 
    # 1. 시작 정점 자신을 제외한 모든 정점까지의 거리를 무한대로 초기화한다.
    
    # 모든 정점들을 거리가 적은 순으로 저장할 priority queue 생성
    queue = []
    heapq.heappush(queue, [distances[start], start])  
        # queue 라는 힙에 [거리, 시작점] 라는 리스트를 추가함
  

    while queue: 
        # 3. 우선순위 큐에서 인접 정점을 하나씩 차례대로 꺼냄, (A의 인접노드 B, C 를 방문한다고 가정)
        current_distance, current_node = heapq.heappop(queue) 
            # current distance = 8, current_node = B

        if distances[current_node] < current_distance: 
        #3-2. 이미 기록된 인접 정점까지의 거리가 더 짧다면 넘어간다.
        # distances에 기록된 B까지의 거리 (INF) < 9
            continue 
        
        for new_destination, new_distance in graph[current_node].items(): 
        # 현재 노드(B)에서 갈 수 있는 정점들
            distance = current_distance + new_distance 
            # B->C 까지 2 였으면 9+2 = 11 
            if distance < distance[new_destination]: 
            # 11 < A->C까지 (2) 이면? (이 경우에는 no)
                distance[new_destination] = distance 
            # distance[C] = 11
                heapq.heappush(queue, [distance, new_destination]) 
                # queue 라는 힙에 [새 거리, 새 시작점] 이렇게 생긴 리스트를 추가함

    return distances

print(dijkstra(graph, start))