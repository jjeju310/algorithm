def solution(n, times):
    answer = 1e18
    start = 0
    end = max(times) * n
    while start <= end:
        t_sum = 0 
        mid = int((end+start)/2)
        #print(start, mid, end, answer)
        for t in times:
            t_sum += int(mid/t)
        print(t_sum)
        if(t_sum>n):
            end = mid-1
            
        elif(t_sum<n):
            start = mid+1
            
        elif(n==t_sum):
            if(answer > mid):
                answer = mid
            end = mid-1
        
        print(start, mid, end, answer)

    """이 코드의 반례-> 1, [2,2], 2 일 때 2초에 1명이 마치 몸 갈라서 두 심사대에 간거 같은 상황 발생
    t_sum>n 인 경우 최소가 아닐 뿐이지 n명이 모두 심사받을 수 있는 건 맞으니까 t_sum>=n일 때 answer 값을 갱신시켜줘야한다고 이해하자"""    
    return answer

