def solution(citations):
    answer = 0
    h = 0
    citations.sort()
            
    while(True):
        c = countCitation(citations, h)
        if (h > c):
            break
        answer = h
        h += 1
    return answer

def countCitation(citations, h):
    count = 0
    for c in citations:
        if (c >= h):
            count += 1
    return count
            