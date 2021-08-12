'''
Question : 
N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열) 이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
단 회문을 검사할 때 대소문자를 구분하지 않습니다.

# Input Examples : 
5

level
moon
abcba 
soon 
gooG

# Output Examples : 
#level YES
#moon NO
#abcba YES
#soon NO 
#gooG YES

# Outputs
mzc01-jiyoon@MZC01-JIYOON algorithm % /usr/local/bin/python3 /Users/mzc01-jiyoon/Desktop/algorithm/8-2.palindrome.py
#SOON NO
#ABCBA YES
#MOON NO
#LEVEL YES
#GOOG YES
'''

import sys

input = {"level", "moon", "abcba" , "soon" , "gooG"}
n = len(input) # Input is going to be 5 words

for word in input:
    word = word.upper() # Convert to Uppercase
    size = len(word) # Length of the "word"
    
    for j in range(size //2):  
        if word[j] != word[-1-j]: # Python counts index from -1
            print(f'#{word} NO')
            break
    else:
        print(f'#{word} YES')
