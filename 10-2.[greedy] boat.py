def solution(people, limit):
    answer = 0
    people.sort()

    if len(people) == 1:
        return 1
    
    # 인덱스
    first = 0
    last = len(people)-1 

    while True:
        if last == first:  # 
            answer +=1
            break
        
        if last < first: # 보트를 다 탄 경우
            break

        if people[first]+ people[last] <= limit: #Case 1: 가장 가벼운애 + 가장 무거운애 했는데 Limit 안넘으면? ->  가벼운애 + 무거운애 배에 태움 
            answer +=1  # 보트 하나 더하고
            first +=1  #인덱스 앞으로
            last -=1  # 가장 마지막 인덱스 뒤로 

        else: # 그냥 한명만 나간 경우
            last-=1
            answer +=1 

    return answer