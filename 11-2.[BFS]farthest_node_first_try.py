from collections import defaultdict

def solution(n, edge):
    answer = 0
    graph_dict = defaultdict(list)
    for i,j in edge:
        graph_dict[i].append(j)
    print(f'graph_dict solution: {graph_dict}')
    
    max = 0
    len_list = []
    for j in graph_dict.values(): # dict_values([[6, 2], [3], [3, 2], [4], [2]])
        len_list.append(len(j))
        
        if len(j) > max:
            max = len(j)
            
    print(f'max {max}')
    print(f'len_list {len_list}')
    answer = len_list.count(max)
    print(f'answer {answer}')
    
    return answer
    '''
    graph_dict: defaultdict(<class 'list'>, {3: [6, 2], 4: [3], 1: [3, 2], 2: [4], 5: [2]})
    '''