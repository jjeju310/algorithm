def solution(citations):
    citations = sorted(citations)
    citations.reverse()
    answer = 0
    sumn = 0
    for idx, n in enumerate(citations):
        print(n, idx+1)
        if (n == idx+1):
            answer = idx+1
            break
        elif (n<idx+1):
            answer = idx
            break
        sumn += n
    print(citations)
    if (answer==0 and sumn!=0):
        answer=len(citations)
    return answer