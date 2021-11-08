def main(bridge_length, weight, truck_weights):
    time = 0
    trucks_on_bridge = [0] * bridge_length  # 올라온 트럭을 담는 리스트

    while len(trucks_on_bridge)>0: 
        time += 1
        trucks_on_bridge.pop(0) 
        if(len(truck_weights)>0): # 자 이제 트럭을 올려보자
            if sum(trucks_on_bridge)+truck_weights[0] <= weight: 
                trucks_on_bridge.append(truck_weights.pop(0))
            else: # weight를 넘어버린 경우? 아무것도 안올라갔으니 
                trucks_on_bridge.append(0)  # 리스트에 0 추가
    return time

if __name__ == '__main__':
    main(2, 10, [7,4,5,6])