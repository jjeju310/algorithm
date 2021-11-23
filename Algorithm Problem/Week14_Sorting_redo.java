package AlgorithmProblem;

import java.util.Arrays;

public class Week14_Sorting_redo {
  public int solution(int[] citations) {
    int answer = 0;
    Arrays.sort(citations);
    int n = citations.length;

    for(int i = 0; i < n; i++) {
      int hIndex = n - i;
      if(hIndex <= citations[i]) {
        answer = hIndex;
        break;
      }
    }
    return answer;
  }
}
