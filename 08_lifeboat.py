def solution(people, limit):
    answer = 0
    people.sort()
    people.reverse()

    l = 0
    r = len(people)-1

    while (l<r):
        l_weight = people[l]
        r_weight = people[r]
        if (l_weight+r_weight) <= limit:
            answer += 1
            l +=1
            r -=1
        elif (l_weight+r_weight) > limit:
            answer +=1
            l += 1
    if(l==r):
        answer += 1 
    
    return answer