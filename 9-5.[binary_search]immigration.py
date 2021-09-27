'''
Date : 2021/09/26
Question: https://programmers.co.kr/learn/courses/30/lessons/43238

'''
def solution(n, times):
    answer = 0
    
    left = 1
    right = max(times) * n # 제일 비효율적인 면접관이 심사를 다했을 때 최댓값
    
    while (left <= right):
        done_ppl = 0
        mid = (left+right) // 2
        
        for time in times : # 7, 10.. 
            done_ppl += mid // time 
            
            if done_ppl >= n: # 한 명 심사관으로도 처리해버린 경우
                break
            
        if done_ppl >= n: 
            '''
            mid 시간 동안에 사람들 다 처리한 경우 
            1. answer값 기록
            2. right를 옮겨서 mid값 줄임
            '''
            answer = mid
            right = mid-1
            
        elif done_ppl < n: 
            '''
            mid 시간 동안에 처리 못한 경우 
            1. left 를 옮겨서 mid 값 올림
            2. answer값 그대로
            '''
            left = mid + 1
            
    return answer