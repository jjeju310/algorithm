package AlgorithmProblem;

import java.util.*;

public class Week13_Graph2 {
  public int solution(int n, int[][] results) {
    int[][] rec = new int[n][n];
    int INF = 100001;

    for(int i = 0; i < n; i++) {
      for(int j = 0; j < n; j++) {
        rec[i][j] = INF;
      }
      rec[i][i] = 0;
    }

    for(int i = 0; i < results.length; i++) {
      rec[results[i][0]-1][results[i][1]-1] = 1;
    }

    for(int k = 0; k < n; k++) {
      for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
          if(rec[i][j] > rec[i][k] + rec[k][j]) {
            rec[i][j] = rec[i][k] + rec[k][j];
          }
        }
      }
    }

//    for(int[] score : rec) {
//      System.out.println(Arrays.toString(score));
//    }

    int answer = 0;
    for(int i = 0; i < n; i++) {
      boolean flag = true;
      for(int j = 0; j < n; j++) {
        if(rec[i][j] == INF && rec[j][i] == INF) {
          flag = false;
          break;
        }
      }
      if(flag) {
        answer++;
      }
    }
    return answer;
  }
}
