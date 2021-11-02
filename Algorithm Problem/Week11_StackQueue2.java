package AlgorithmProblem;

import java.util.*;

// 프로그래머스 - 다리를 지나는 트럭 (https://programmers.co.kr/learn/courses/30/lessons/42583)
public class Week11_StackQueue2 {
  public int solution(int bridge_length, int weight, int[] truck_weights) {
    Queue<Integer> bridge = new LinkedList<>();
    int sum = 0;
    int time = 0;
    int answer = 0;

    for(int i = 0; i < truck_weights.length; i++) {
      int truck = truck_weights[i];

      while(true) {
        if(bridge.isEmpty()) {
          bridge.add(truck);
          time++;
          sum += truck;
          break;
        } else if(!bridge.isEmpty() && bridge.size() != bridge_length) {
          if(truck + sum <= weight) {
            bridge.add(truck);
            time++;
            sum += truck;
            break;
          } else {
            bridge.add(0);
            time++;
          }
        } else {
          sum -= bridge.poll();
        }
      }
    }
    answer = time + bridge_length;
    return answer;
  }
}
