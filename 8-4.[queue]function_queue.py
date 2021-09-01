import sys
from collections import deque
from operator import add

progresses = [93, 30, 55]
speeds = [1, 30, 5]

answer=[]

queue_progresses = deque(progresses) # 작업 개수 리스트를 큐로 변환
queue_speed = deque(speeds) # 속도 리스트를 큐로 변환

while queue_progresses:
    count = 0 # 배포할때마다의 기능 개수
    
    # 기능 개발이 하나만 남은 경우 날짜와 상관없이 하나만 배포하니깐 answer=1을 추가하고 종료
    if len(queue_progresses)==1:
        answer.append(1)
        break
    
    # 개발 진행도
    queue_progresses = deque(map(add, queue_progresses, queue_speed)) # speed + 진행도

    while queue_progresses:
        if queue_progresses[0]>=100: # 100%가 넘어가면 pop
            queue_progresses.popleft()
            queue_speed.popleft()
            count += 1
        else:
            break
    
    if count != 0:
        answer.append(count)
    
    print(f'[answer]{answer}')