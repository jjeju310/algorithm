'''
- heapq를 사용하는 이유 : 현재시간을 기준으로 대기하는 job들 중에서 무조건 가장 짧은 요청을 먼저 수행함
- 우선순위큐를 사용해서 항상 최솟값을 꺼냄

- jobs_heap[]
- now : 현재 시각
- last : 지난 시각
- count : 처리한 작업의 개수

작업이 수행할동안 나머지 작업들을 heap에 넣음
작업이 끝나면 heap에서 작은 작업을 실행시킴

1. jobs 라는 리스트를 정렬해줌 (시작시간이 0초인애가 있으면 빨리 시작해주기 위해서)
2. count: 작업이 끝났는지 검사해줌 / last = 현재 작업이 시작한 시간
3. wait : 일이 진행되는 동안 기다리는 다른 작업들을 저장하는 힙
4. time : 현재 시간인데, jobs의 첫번째 요소의 시간으로 초기화함 (어떤 작업이 진행되고 있는데 )
5. length : 리스트의 길이
6. answer : 
'''
import heapq

# jobs = []
def solution(jobs):
    jobs.sort()
    count, last = 0, -1 
    wait = []
    time = jobs[0][0]
    length = len(jobs)
    answer = 0

    while count < len(jobs):
        for s, t in jobs:
            if last  < s <= time:
                heapq.heappush(wait, (t, s)) # 실행시간이 가장 작은걸로 정렬해야하니깐 거꾸로 넣음
        
        if len(wait) > 0:  # 작업이 끝난 시점에 힙에 남아있는 작업이 있으면
                last = time
                term, start = heapq.heappop(wait)
                count += 1
                time += term # 현재 시간에 걸린 시간 더해줌
                answer += (time - start)
        else:
            time += 1 # 요소가 없으면 시간을 기다림 (?)

    average_answer = answer // length
    return average_answer