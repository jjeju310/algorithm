package AlgorithmProblem;

import java.util.Arrays;

// 프로그래머스 - 구명보트(https://programmers.co.kr/learn/courses/30/lessons/42885)
public class Week16_Greedy_redo {
  public int solution(int[] people, int limit) {
    Arrays.sort(people); // 50 50 70 80
    int answer = 0;

    int min = 0;
    for(int max = people.length - 1; min <= max ; max--) {
      if(people[min] + people[max] <= limit) {
        answer++;
        min++;
      } else {
        answer++;
      }
    }
    return answer;
  }
}
