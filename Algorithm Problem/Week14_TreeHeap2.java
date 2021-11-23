package AlgorithmProblem;

import java.util.*;

// 프로그래머스 - 여행경로 (https://programmers.co.kr/learn/courses/30/lessons/43164)
public class Week14_TreeHeap2 {
  boolean[] visited;
  ArrayList<String> allRoute;

  public String[] solution(String[][] tickets) {
    String[] answer = {};
    int cnt = 0;
    visited = new boolean[tickets.length];
    allRoute = new ArrayList<>();

    dfs("ICN", "ICN", tickets, cnt);

    Collections.sort(allRoute);
    answer = allRoute.get(0).split(" ");

    return answer;
  }

  public void dfs(String start, String route, String[][] tickets, int cnt){
    if(cnt == tickets.length) {
      allRoute.add(route);
      return;
    }

    for(int i=0; i<tickets.length; i++){
      if(start.equals(tickets[i][0]) && !visited[i]) {
        visited[i] = true;
        dfs(tickets[i][1], route+" "+tickets[i][1], tickets, cnt+1);
        visited[i] = false;
      }
    }
  }
}