def solution(bridge_length, weight, truck_weights):
    answer = 0
    idx = 0
    
    bridge_weight = 0
    bridge = []
    
    total_sec= 0
    in_sec = []
    
    done_truck = []
    
    while(len(done_truck) != len(truck_weights)):
        total_sec += 1
        
        if((total_sec - bridge_length) in in_sec):
            del in_sec[0]
            truck = bridge[0]
            del bridge[0]
            done_truck.append(truck)
            bridge_weight -= truck
        
        if(len(truck_weights) > idx):
            if(bridge_length >= len(bridge)):
                if(weight >= bridge_weight + truck_weights[idx]):
                    in_sec.append(total_sec)
                    bridge.append(truck_weights[idx])
                    bridge_weight += truck_weights[idx]
                    idx += 1

    return total_sec