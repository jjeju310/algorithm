'''
첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000)
모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다.
둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다.
셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다.
이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
'''
import sys
import heapq


def print_answer(distance, node_cnt):
    INF = int(1e9)

    for i in range(1, node_cnt + 1):
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])


def dijkstra(start, node_graph, distance):
    queue = []

    heapq.heappush(queue, (0, start))  # 가중치 0원에 start에서 시작하는걸로 초기화
    distance[start] = 0

    while len(queue) > 0:
        dist, now = heapq.heappop(queue)  # Queue 생성

        # 1) 현재 지점을 들러서 가는게 더 손해인 경우
        if dist > distance[now]:
            continue

        # 2) 갈 수 있는 서브 노드들 탐색
        for sub_node in node_graph[now]:  # sub_node = [(2,2), (3,3)] 의 (2,2)
            cost = dist + sub_node[1]  # 딸린 서브노드의 가중치

            if cost < distance[sub_node[0]]:  # 서브노드를 거쳐서 가는 것이 distance에 원래 저장되어 있 최단 거리보다 짧으면?
                distance[sub_node[0]] = cost  # 2-1) distance 갱신
                heapq.heappush(queue, (cost, sub_node[0]))


def main():
    sys.stdin = open("input.txt", "r")
    node_cnt, vertex_cnt = map(int, input().split())  # node_cnt :정점의 개수 , vertex_cnt: 간선의 개
    start = int(input())  # 시작 정점 번호
    INF = int(1e9)

    node_graph = [[] * (node_cnt+1) for _ in range(node_cnt+1)]  # node_graph
    distance = [INF] * (node_cnt+1)

    # u에서 v까지 가는데 가중치 w
    for _ in range(vertex_cnt):
        u, v, w = map(int, input().split())
        node_graph[u].append((v, w))  # ex. [[], [(2, 2), (3, 3)], [(3, 4), (4, 5)], [(4, 6)], [], [(1, 1)]]
    print(node_graph)
    dijkstra(start, node_graph, distance)

    print_answer(distance, node_cnt)
    return


if __name__ == "__main__":
    main()