package AlgorithmProblem;

import java.util.Arrays;

// 프로그래머스 - 입국심사 (https://programmers.co.kr/learn/courses/30/lessons/43238)
public class Week15_BinarySearch_redo {
  public long solution(int n, int[] times) {
    long answer = 0;
    Arrays.sort(times);
    long min = 1;
    long max = (long) n * times[times.length - 1];

    while (min <= max) {
      long mid = (min + max) / 2;
      long people = 0;
      for(int i = 0; i < times.length; i++) {
        people += mid / times[i];
      }
      if(people < n) {
        min = mid + 1;
      } else {
        max = mid - 1;
        answer = mid;
      }
    }

    return answer;
  }
}
