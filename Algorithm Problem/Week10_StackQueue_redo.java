package AlgorithmProblem;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

// 프로그래머스 - 기능개발 (https://programmers.co.kr/learn/courses/30/lessons/42586) 다시 풀어보기
public class Week10_StackQueue_redo {
  public int[] solution(int[] progresses, int[] speeds) {
    Queue<Integer> left = new LinkedList<>();
    ArrayList<Integer> answer = new ArrayList<>();
    int count = 0;

    for(int i = 0; i < progresses.length; i++) {
      // 100(x)
      left.add((int)Math.ceil((100.0-progresses[i])/speeds[i]));
    }

    while(!left.isEmpty()) {
      // count++; (x)
      count = 1;
      int released = left.poll();

      while(!left.isEmpty() && released >= left.peek()) {
        left.poll();
        count++;
      }

      answer.add(count);
    }

    // int[] 를 ArrayList<Integer>로 리턴하기 위한 변환과정(잊지말자)
    return answer.stream().mapToInt(Integer::intValue).toArray();
  }
}
