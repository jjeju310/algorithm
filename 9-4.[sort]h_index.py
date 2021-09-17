def solution(citations):
    citations.sort()
    len_citations = len(citations)
    for i in range(len_citations):
        if citations[i] >= len_citations-i: # 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번)
            return len_citations-i
    return 0