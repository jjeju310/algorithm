import collections


def solution(tickets):
    answer = []
    routes = collections.defaultdict(list)
    stack = ['ICN']

    # 1.정렬이 잘 된 routing table 만들기 (dict)
    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])

    '''
    routes = {
    'ICN': ['SFO', 'ATL'], 
    'SFO': ['ATL'], 
    'ATL': ['ICN', 'SFO']
    }
    '''
    sorted_routes = _sort_routes(routes)
    # 2. stack 에 넣고 routing table 에 갈 수 있는 경로 있는 없는지 판단
    print(sorted_routes)
    while stack:
        current_location = stack[-1]
        print(f'{stack}: {current_location}')

        # 2-1. 경로 없는 경우 : answer.append
        if not routes[current_location]:
            answer.append(stack.pop())
        # 2-2. 경로 있는 경우 : routes.pop 하고 stack.push
        else:
            next_location = sorted_routes[current_location].pop()
            print(f'next location: {current_location} -> {next_location}')
            stack.append(next_location)

    answer.reverse()
    print(f'answer : {answer}')
    return


def _sort_routes(routes):
    # for route in routes:
    for k, v in routes.items():
        v.sort(reverse=True)

    # print(routes.items())
    '''
    new_routes = [
    ('ICN', ['ATL', 'SFO']), 
    ('SFO', ['ATL']), 
    ('ATL', ['ICN', 'SFO'])]
    '''
    return routes

def main():
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    solution(tickets)


if __name__ == "__main__":
    main()
