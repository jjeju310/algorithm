import heapq


def solution(jobs):
    jobs.sort()
    total_spent_time = 0  # 작업하는데 소요한 총 시간
    finished_job_cnt = 0  # 끝난 작업 개수
    finished_time_of_previous_job = -1  # 지난 작업 끝난 시간
    remained_jobs = []  # list to push to heap
    total_job_cnt = len(jobs)
    current_time = jobs[0][0]  # 현재 시간: 0초부터 시작

    while finished_job_cnt < total_job_cnt:
        # jobs 를 돌면서 현재 진행되는 작업과 겹치는지 확인해야함 / push to the heap 시간 짧은 순서대로
        for start, time in jobs:  # ex. A: start = 0, time=3 / B: start = 1, time = 9 / C: start = 2, time = 6
            if finished_time_of_previous_job < start <= current_time:
                heapq.heappush(remained_jobs, (time, start))

        if len(remained_jobs) > 0:  # 디스크에 남은 작업 있으면?
            finished_time_of_previous_job = current_time
            time, start = heapq.heappop(remained_jobs)   # heap 에서 하나 꺼
            finished_job_cnt += 1
            current_time += time  # 작업 하는데 시간 time 만큼 걸렸으니깐 현재 시간 업데이트해줌
            wait_time = current_time - start  # 요청부터 (1초에 요청했음) 실제 시작한 시간(2초)까지 대기한 시간
            total_spent_time += wait_time   # 대기시간 더해줌냄

        else:  # 남은 작업 없으면 1초씩 기다림
            current_time += 1

    total_spent_time = total_spent_time // total_job_cnt
    print(total_spent_time)
    return total_spent_time


def main():
    jobs = [[0, 3], [1, 9], [2, 6]]
    solution(jobs)


if __name__ == "__main__":
    main()