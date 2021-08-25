def solution(progresses, speeds):
    re_pro = []
    work_dur = []
    for i in range(len(progresses)):
        #남은 진도 구하기
        re_pro.append(100 - progresses[i]) 
    for i in range(len(speeds)):
        #남은 진도 속도로 나눠떨어지면 작업기간 리스트에 그냥 넣음
        if(re_pro[i]%speeds[i]==0):
            work_dur.append(re_pro[i]/speeds[i]) 
        #소수점이 나오면 몫에 +1 에서 넣음
        else:
            work_dur.append(int(re_pro[i]/speeds[i])+1) 
            
    # work_dur = [15,2,10,9,1,20,1] -> answer = [5, 2]
    
    answer = [1] # work_dur[0]이 첫 배포의 기준이 되므로 answer[0]=1
    idx = 0 # answer 리스트의 인덱스 컨트롤을 위한 변수
    
    for i in range(len(work_dur)-1):
        if(work_dur[i+1]>work_dur[i]):
            if(work_dur[i+1]>max(work_dur[0:i+1])): # i+1 번째 원소가 i 번째 원소 보다 크면서 i+1 번째 원소의 모든 이전 작업보다 오래걸리는거면 i 번째 원소의 배포는 이미 끝난 상태이므로 answer[i의 idx + 1] = 1
                answer.append(1)
                idx +=1
            else: # i+1 번째 원소가 이전 원소보다 크기는 하지만 그 이전의 이전의 이전...의 원소 중에 i+1 번째보다 더 큰게 있다면 더 큰거의 배포일에 포함되므로 answer[i의 idx] += 1 
                answer[idx] += 1    
        else: # 이전 원소보다 작으면 무조건 그 이전 원소 배포일에 포함되므로 answer[i(이전원소)의 idx] += 1 
            answer[idx] += 1

    return answer