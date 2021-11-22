'''
input :
20  #지폐의 금액
3 # 동전의 가지수 3개
5 3 # 5원짜리 3개
10 2  # 10원짜리 2개
1 5  #1원짜리 5개
'''

import sys

sys.stdin = open("input.txt", "r")


def DFS(L, sum):
    global answer
    if L == k:  # 도착지점에 왔을 때
        answer += 1

    else:
        for i in range(cn[L] + 1):
            DFS(L + 1, sum + (i * count[L]))


if __name__ == "__main__":
    t = int(input())  # 지폐의 금액
    k = int(input())  # 동전의 가지수
    coin = list()  # coin = [5,10,1]
    count = list()  # count = [3,2,5]

    for i in range(k):
        a, b = map(int, input().split())
        coin.append(a)
        count.append(b)

    answer = 0
    DFS(0, 0)
