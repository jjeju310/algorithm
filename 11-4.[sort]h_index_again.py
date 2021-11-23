import collections


def count_referenced(given_citation, citations):
    referenced_cnt = 0
    for citation in citations:
        if given_citation <= citation:
            referenced_cnt += 1

    print(f'{given_citation}"s referenced_cnt: {referenced_cnt}')
    return referenced_cnt


def find_max_index(citation_referenced_dict):
    h_index = min(citation_referenced_dict.items())
    for k, v in citation_referenced_dict.items():
        if k > h_index and k == v:
            h_index = k
    print(h_index)
    return h_index


def solution(citations):
    answer = 0

    citation_referenced_dict = {}

    for citation in citations:
        citation_referenced_dict[citation] = count_referenced(citation, citations)

    print(f'citation_referenced_dict: {citation_referenced_dict}')
    find_max_index(citation_referenced_dict)
    return answer


def main():
    citations = [10, 100]
    solution(citations)


if __name__ == "__main__":
    main()
