import heapq

def solution(jobs):
    '''
    1. jobs를 시작시간 별로 정렬한다.
    2. while문: 끝난 작업개수 < 총 작업개수

        2-1. jobs를 순회하면서 heap에 실행시간이 작은 순서대로 넣는다. (넣을 때 힙에 거꾸로 넣음 실행시간 순서대로 정렬되라고)
        2-2. other jobs에 작업이 있으면:
                    2-2-1. 현재 작업의 시작시간으로 현재시간을 넣음
                    2-2-2. 힙에서 현작업 꺼냄
                    2-2-3. 끝난 작업수 +1
                    2-2-4. 현재 시간에 걸린 시간을 더해줌
                    2-2-5. answer += 대기시간(현재 시간 - 원래 시작했어야 하는 시간)
        2-3. 없으면:
            current_time += 1 
    3. answer 계산 (총 걸리시간 / job개수)
    '''
    finished_jobs_cnt = 0
    total_jobs_cnt = len(jobs)
    answer = 0
    current_job_start_time = -1
    current_time = 0
    jobs.sort()
    other_jobs = []

    while finished_jobs_cnt < total_jobs_cnt:
        for s, t in jobs:
            if current_job_start_time < s < current_time:
                heapq.heappush(other_jobs, (t,s)) 
        
        if len(other_jobs) > 0:
            current_job_start_time = current_time
            time, start =heapq.heappop(other_jobs)
            finished_jobs_cnt +=1
            current_time += time
            wait_time = current_time - start
            answer += wait_time

        else:
            current_time+=1
    average_answer = answer // total_jobs_cnt
    return average_answer