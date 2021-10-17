def solution(m, n, puddles):
    answer = 0
    # 1. map[i][j] 를 모두 0으로
    way = [[0] * (m+1) for _ in range(n+1)]
    
    way[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            
            if i == 1 and j==1: 
                continue
            
            elif [j,i] not in puddles: # 물웅덩이 아닐 때
                way[i][j] += (way[i-1][j] + way[i][j-1]) 
    
    answer = way[n][m] % 1000000007
    return answer