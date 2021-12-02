def solution(files):
    answer = []
    sorted_files = []
    check = 0
    
    for f in files:
        head_idx = 0
        while True:
            if len(f)-1 < head_idx: #인덱스 초과하는 에러 없도록
                break
            if f[head_idx].isdigit(): #숫자 나오면 끊기
                break
            
            head_idx += 1
        num_idx = head_idx
        while True:
            if len(f)-1 < num_idx: #인덱스 초과하는 에러 없도록
                break
            if not f[num_idx].isdigit(): #숫자 외 문자 나오면 끊기
                break
            if num_idx == head_idx+5: #문제에서 숫자영역은 최대 다섯글자라고 정의
                break
            num_idx += 1
        sorted_files.append((f[0:head_idx], f[head_idx:num_idx], f[num_idx:]))
    print(sorted_files)
    
    sorted_files.sort(key = lambda x : (x[0].lower(), delete_zero(x[1]))) #head 대소문자 구분없이 정렬 우선, head 같을 경우 number에서 앞에 붙은 0과 관계없이 정렬, 파이썬 사랑해
    print(sorted_files)
    
    for f in sorted_files:
        name = f[0]+f[1]+f[2]
        answer.append(name)
        
    print(answer)
    return answer

def delete_zero(x):
    idx = 0
    while True:
        if not x[idx] == 'a':
            break
        idx+=1
    return (int(x[idx:]))