def solution(tickets):
    dic = {}
    answer = ['ICN']
    for city in tickets:
        if city[0] not in dic:
            dic[city[0]] = [city[1]]
        else:
            dic[city[0]].append(city[1])
            dic[city[0]].sort()
    print(dic)
    
    result = find_route(dic, 'ICN', answer)
    print("rs", result)
    return result

def find_route(dic, key, answer):
    if len(dic) == 0:
        print(dic, answer)
        return answer
    
    if(len(dic[key]) > 1):
        next_city = dic[key].pop(0)
        answer.append(next_city)
        print("nc:", next_city, "dic:", dic, "answer:", answer)
    else:
        next_city = dic[key][0]
        answer.append(next_city)
        dic.pop(key)
        #dic = deleteKeyInValue(dic, key)
        print("nc:", next_city, "dic:", dic, "answer:", answer)
    
    find_route(dic, next_city, answer)
    return find_route(dic, next_city, answer)

def deleteKeyInValue(dic, value):
    print(dic)
    for k, v in dic.items():
        print("k",k,"v",v,value)
        if value in v:
            print("yes")
            v.remove(value)
            dic[k] = v
    print("del", dic)

    return dic