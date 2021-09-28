def solution(n, times):
    max_time = n*times[len(times)-1]
    answer = -1
    start = 0
    end = max_time
    
    while (start <= end) :
        #중간점을 찾는다
        #중간점과 times의 원소를 모두 나눠서 더한다(n_sum)
        #n과 비교한다
        #n_sum이 n과 같다고 하여 mid가 최소값이 아닐 수도 있으므로 멈추지 않고 이분탐색을 끝까지 진행한다
        #시작과 끝 값을 바꾼다 
        mid = int((start + end)/2)
        print("mid:",mid)
        n_sum = 0
        for t in times:
            n_sum += int(mid / t)
        print("n_sum", n_sum)
        if(n_sum < n):
            start = mid + 1
        elif(n_sum >= n):
            answer = mid
            end = mid-1
            
    return answer
    