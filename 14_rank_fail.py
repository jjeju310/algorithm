def solution(n, results):
    answer = 0
    graph = [[0] * (n+1) for _ in range(n+1)] # 승패여부를 저장할 그래프
    
    # 이기면 1, 지면 -1로 그래프에 저장
    for win, lose in results:
        graph[win][lose] = 1
        graph[lose][win] = -1
    
    # 플로이드 워셜 수행
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if a != b and graph[a][b] == 0: # 자기 자신이 아니면서 아직 승패여부를 알 수 없는 노드라면
                    if graph[a][k] == 1 and graph[k][b] == 1: # a가 k를 이기고 k가 b를 이기면 a가 b를 이김 
                        graph[a][b] = 1 
                    elif graph[a][k] == -1 and graph[k][b] == -1: # a가 k에게 지고 k가 b에게 지면 a가 b에게 짐 
                        graph[a][b] = -1

    # 순위를 매길 수 있는 선수 세기
    for i in range(1, n+1):
        if graph[i][1:].count(0) == 1:
            answer += 1
                
    return answer