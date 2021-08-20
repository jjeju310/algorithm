"""프로그래머스, 전화번호 목록 문제 : 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다."""

def solution(phone_book):
    
    sorted_book = sorted(phone_book) #접두사를 찾으려면 문자열의 앞머리가 같아야하므로 효율성을 위해 정렬
    
    result_table = {}
    
    for i in range(len(sorted_book)-1):
        if(sorted_book[i+1].startswith(sorted_book[i])):
            if('false' not in result_table):
                result_table['false'] = 1    
            else: 
                result_table['false'] +=1
        else:
            if('true' not in result_table):
                result_table['true'] = 1    
            else: 
                result_table['true'] +=1
    
    if('false' in result_table):
        answer = False
    else:
        answer = True
    
    
    return answer