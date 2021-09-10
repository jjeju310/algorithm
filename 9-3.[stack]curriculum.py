'''
# Input Examples : 
CBA
3
CBDAGE
FGCDAB
CTSBDEA



# Output Examples : 
#1 YES
#2 NO
#3 YES
----------------

# Outputs
mzc01-jiyoon@MZC01-JIYOON algorithm % /usr/local/bin/python3 /Users/mzc01-jiyoon/Desktop/algorithm/practice.py
#1 YES
#2 NO
#3 YES
'''

import sys 
from collections import deque
sys.stdin=open("input.txt", "r")

essential_classes = input()
classes_cnt = int(input())
for i in range(classes_cnt):
    curriculum = input() #ex. C
    curriculum_que = deque(essential_classes)
    for x in curriculum: #순서가 통과했는지 
        if x in curriculum_que : # 필수 이수 과목에 있는지 확인 (과목 다 이수했는지 먼저 확인)
            if x != curriculum_que.popleft(): # 앞에서 꺼낸 필수과목의 맨 앞자료와 현 자료 일치하지 않으면
                print(f'#{i+1} NO')
                break
    
    else:
        if len(curriculum_que)==0: # 필수과목을 모두 다 포함 시켰는지 확인
            print(f'#{i+1} YES')
        else:
            print(f'#{i+1} NO')
