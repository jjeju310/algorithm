import sys
sys.stdin=open("input.txt", "r")
'''
상태트리를 그리는데, 3가닥으로 뻗음
왼쪽 가닥 -> 왼쪽 저울에서 잼 (sum+= 추 무게)
중간 가닥 -> 오른쪽 저울에서 잼 (sum-= 추 무게 물의 그릇이 왼쪽에 있는 경우를 의미)
오른쪽 가닥 -> 재지 않음
'''

def DFS(L, sum): # L: G를 접근하는 인덱스, sum : 측정할 수 있는 추의 무게
    global result
    if L == n: # 종료지점
        if 0 < sum <= total_sum: #추의 무게의 합은 0이상 총 추 무게의 합 이하
            result.add(sum)
    else: # 가지를 3가지 경우의 수로 뻗어서 탐색함
        DFS(L+1, sum + g_list(L)) # 추를 왼쪽에 놓는 경우
        DFS(L+1, sum - g_list(L)) # 추를 오른쪽에 놓는 경우
        DFS(L+1, sum) # 추를 무게를 재는데 사용 안함

n = int(input())
g_list = list(map(int, input().split()))
total_sum = sum(g_list) # 추의 무게의 총함
result = set() # 중복을 제거하면서 값을 추가하는 자료구조 set
DFS(0,0)
print(total_sum-len(result)) #측정하지 못하는 경우의 수 출력