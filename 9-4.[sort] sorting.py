'''
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
5
5
4
3
2
1

첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

1
2
3
4
5
'''
import sys 
sys.stdin=open("input.txt", "r")

num = input()
origin_list = [list(map(int, input().split())) for _ in range(num)]  # note) map(int, input()).split() = 1 line
origin_list.sort()
origin_set = set(origin_list)
for i in origin_set:
    print(i)


