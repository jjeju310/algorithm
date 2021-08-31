'''
# Input Examples : 
3 7

# Output Examples : 
3, 6, 2, 7, 5, 1, 4

#output
mzc01-jiyoon@MZC01-JIYOON algorithm % /usr/local/bin/python3 /Users/mzc01-jiyoon/Desktop/algorithm/8_4.py
3, 6, 2, 7, 5, 1, 4
'''
import sys
sys.stdin = open("input.txt", "r")
n,k = map(int, input().split())

round_list = []
result = []
pop_index = 0 # 제거할 node의 index

# make list
for i in range(n):
    round_list.append(i+1) # i starts with 0, so append (i+1)


for j in range(n):
    pop_index += k-1 # 0번부터 시작

    if pop_index > len(round_list): # 주기가 리스트보다 길면 인덱스 에러나니깐 ex.8명 있는데 19번째 pop -> 19 % 8 = 3번째 pop
        pop_index = pop_index % len(round_list) 
    
    result.append(str(round_list.pop(pop_index)))

print(", ".join(result))


