from collections import deque


def solution(n, edge):
    answer = 0
    node_graph = [([]*n) for _ in range(n+1)]
    
    for x, y in edge:  # 연결된 노드들 저장
        node_graph[x].append(y) 
        node_graph[y].append(x)
    
    visited = [0]*(n+1)  # 방문한 노드들이 있으면 몇개인지 저장되는 리스트
    visited[1] = 1  # 1번 노드는 방문했다고 가정
    
    search_queue = deque([1])  # 1번 노드부터 탐색 시작하기 위해 큐에 넣음
    
    # 탐색
    while len(search_queue) > 0:
        n = search_queue.popleft()  # queue 에 들어있는 첫번째 요소 꺼냄
        for i in node_graph[n]:
            if visited[i] == 0:
                search_queue.append(i)
                visited[i] = visited[n]+1  # 방문했음
    
    answer = visited.count(max(visited))
    print(f'answer: {answer}')
    return answer


def main():
    n = 6
    edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    solution(n, edge)


if __name__ == "__main__":
    main()