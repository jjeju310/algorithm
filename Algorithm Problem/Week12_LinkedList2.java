package AlgorithmProblem;

import java.util.*;

// 프로그래머스 - 가장 먼 노드(https://programmers.co.kr/learn/courses/30/lessons/49189)
class Week12_LinkedList2 {
  public int solution(int n, int[][] edge) {
    int answer = 0;

    // 그래프 구현
    ArrayList<ArrayList<Integer>> list = new ArrayList<ArrayList<Integer>>(); // 리스트가 리스트를 원소로 가짐
    for(int i = 0; i < edge.length; i++) {
      list.add(new ArrayList<Integer>());
    }

    // 노드 연결
    int a, b;
    for(int[] node : edge) {
      a = node[0];
      b = node[1];
      list.get(a).add(b);
      list.get(b).add(a);
    }

    int[] count = new int[n+1]; // 1과의 거리 저장
    boolean[] visited = new boolean[n+1]; // 노드 방문여부
    Queue<Integer> queue = new LinkedList<>();
    queue.add(1); // 시작점
    visited[0] = visited[1] = true; // 1부터 시작
    int now;
    while(!queue.isEmpty()) {
      now = queue.poll();
      for(int v : list.get(now)) {
        if(!visited[v]) { // now와 연결된 노드들이 방문하지 않은 곳이다?
          count[v] = count[now]+1; // 1부터의 길이를 저장함
          visited[v] = true;
          queue.add(v); // 이곳과 연결된 노드에 방문하기 위해 큐에 저장
        }
      }
    }

    int max = 0; // 1과 가장 멀리 떨어진 노드와의 길이 저장
    for(int cnt : count) {
      if(max < cnt) {
        max = cnt;
        answer = 1;
      } else if(max == cnt) {
        answer++;
      }
    }
    return answer;
  }
}
