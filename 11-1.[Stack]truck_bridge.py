def main(bridge_length, weight, truck_weights):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    time = 0
    trucks_on_bridge = [0] * bridge_length  # 올라온 트럭을 담는 리스트
    trucks_on_bridge = trucks_on_bridge.reverse()

    while len(trucks_on_bridge):  # ex. trucks_on_bridge = [0,0]  bridge index 만큼
        time += 1
        trucks_on_bridge.pop()  # bridge.pop(0)의 의미: bridge[index]에 트럭이 올라왔다고 가정
        if truck_weights:
            if sum(trucks_on_bridge)+truck_weights[0] <= weight:  # 올라가 있는 애들 + 남은 애들 중에 올라간애... 여기서 pop하면 안됨
                trucks_on_bridge.append(truck_weights.pop(0))
        else:
            trucks_on_bridge.append(0)  # 리스트에 0 추가
    print(time)
    return time
