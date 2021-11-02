from collections import deque

N, K = map(int, input().split())

list = [i for i in range(1, N+1)]
dq = deque(list)

answer = "<"
while(len(dq)!=0):
	dq.rotate(-(K-1))
	answer += str(dq.popleft())+", "

print(answer[0:-2]+">")