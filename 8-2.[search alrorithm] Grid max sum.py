'''
Question : 
55 격자판에 아래롸 같이 숫자가 적혀있습니다.
NN의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합니다. (3-7)


# Input Examples : 
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는 다.
5
10 13 10 12 15 
12 39 30 23 11 
11 25 50 53 15 
19 27 29 37 27 
19 13 30 13 19


# Output Examples : 
155
----------------
# Inputs
mzc01-jiyoon@MZC01-JIYOON algorithm % /usr/local/bin/python3 "/Users/mzc01-jiyoon/Desktop/algorithm/8-2.[search alrorithm] Grid max sum.py"
[10, 13, 10, 12, 15]
[12, 39, 30, 23, 11]
[11, 25, 50, 53, 15]
[19, 27, 29, 37, 27]
[19, 13, 30, 13, 19]

# Outputs
mzc01-jiyoon@MZC01-JIYOON algorithm % /usr/local/bin/python3 "/Users/mzc01-jiyoon/Desktop/algorithm/8-2.[search alrorithm] Grid max sum.py"
155
'''

import sys
sys.stdin = open("input.txt", "r")

n = int(input())

grid_list = [list(map(int, input().split())) for _ in range(n)]  # note) map(int, input()).split() = 1 line
max_value = -21470000 # initialize with very small int

# Get sum of rows, colums
for i in range(n):
    sum1 = sum2 = 0 # sum1 = sum of row, sum2 = sum of column
    for j in range(n):
        sum1+=grid_list[i][j]
        sum2+=grid_list[j][i]
    
    if sum1 > max_value:
        max_value = sum1

    if sum2 > max_value:
        max_value = sum2

# Get sum of cross values
left_cross_sum = 0
right_cross_sum = 0

for i in range(n):
    left_cross_sum += grid_list[i][i] 
    right_cross_sum += grid_list[i][n-i-1]
    
if left_cross_sum > max_value:
    max_value = left_cross_sum

if right_cross_sum > max_value:
    max_value = right_cross_sum

print(max_value)
    

