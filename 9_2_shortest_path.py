import sys
sys.stdin=open("input.txt", "r")
import heapq

v, e = map(int, input().split()) #첫번째 줄 입력 ex. 5 6 5개의 정점 
start = int(input()) # 시작점

graph = [[]for _ in range(v+1)]
for _ in range(e):
    a, b, w = map(int, input().split())
def dijkstra(graph, start):
    distances= {node: float('inf') for node in graph}


dijkstra(start)
for i in range(1, v+1):
    if distance[i] >= INF:
        print("INF")


    if p== INF