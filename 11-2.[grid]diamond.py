'''

# Input Examples : 
7
74 10 31 26 59 16 89 
78 44 49 1 64 33 15 
9 95 70 18 22 25 40 
62 77 28 3 78 75 23 
82 38 20 16 42 1 79 
1 24 2 25 95 26 79 
4 35 46 94 70 44 83 
3
2 0 3
5 1 2
3 1 4


# Output Examples : 
1304
----------------
# Inputs
mzc01-jiyoon@MZC01-JIYOON algorithm % /usr/local/bin/python3 "/Users/mzc01-jiyoon/Desktop/algorithm/8-3.[search_algorithm] Grid_turn.py"
7
74 10 31 26 59 16 89 
78 44 49 1 64 33 15 
9 95 70 18 22 25 40 
62 77 28 3 78 75 23 
82 38 20 16 42 1 79 
1 24 2 25 95 26 79 
4 35 46 94 70 44 83 
3
2 0 3
5 1 2
3 1 4


# Outputs
mzc01-jiyoon@MZC01-JIYOON algorithm % /usr/local/bin/python3 "/Users/mzc01-jiyoon/Desktop/algorithm/8-2.[search alrorithm] Grid max sum.py"
1304
'''
import sys
from typing import List
sys.stdin = open("input.txt", "r")
n=int(input()) # 격자의 개수
land_list = [list(map(int, input().split())) for _ in range(n)]

rotate_cnt = int(input())
for i in range(rotate_cnt):
    h, t, k = map(int,input().split()) # ex. 2,0,3
    if t == 0 : # Left rotation
        for i in range(k):
            first_txt=land_list[h-1].pop(0) # when use pop(), automatically it craves one by one. 처음꺼 꺼내서 마지막으로 넣음
            land_list[h-1].append(first_txt)
    
    else: # Right rotation
        for i in range(k):
            land_list[h-1].insert(0, land_list[h-1].pop()) # 마지막꺼 꺼내서 맨 앞자리에 넣음


# Get sum by Diamond 
result = 0
start =0
end = n-1 

for i in range(n):
    for j in range(start, end+1):
        result +=land_list[i][j]
    
    if i < n//2: # 좁아지는 부분
        start+=1
        end-=1
    else: # 넓어지는 부분
        start -=1
        end +=1 

print(result)

