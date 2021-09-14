import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    skip = -1
    hq = []
    
    while i<len(jobs):
        for j in jobs:
            if skip < j[0] <= now: #아직 안된 작업중에 현시점과 시작시점이 같다면 
                heapq.heappush(hq, [j[1], j[0]]) #힙에 넣는다

        if len(hq) > 0: #힙에 뭔가 대기하고 있다면
            current = heapq.heappop(hq) #하나 꺼내서
            skip = now # 작업완료된 시점을 현재시점으로 바꿔주고
            now += current[0] # 현재시점에 작업에 소요된 시간을 더해준다
            answer += (now - current[1]) # answer에 대기시간+작업소요시간 더해준다
            i += 1
        else:
            now += 1 # 현재 처리할 작업이 없다면 다음시점으로 넘어간다
    
    return int(answer/len(jobs))