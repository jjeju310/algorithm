package AlgorithmProblem;

import java.util.*;

class Node implements Comparable<Node> {
  private int index;
  private int distance;

  public Node(int index, int distance) {
    this.index = index;
    this.distance = distance;
  }

  public int getIndex() {
    return this.index;
  }

  public int getDistance() {
    return this.distance;
  }

  @Override
  public int compareTo(Node other) {
    if(this.distance < other.distance) {
      return -1;
    }
    return 1;
  }
}

public class Week12_Graph_redo {
  public static final int INF = (int) 1e9;
  public static int V, E, start;
  public static ArrayList<ArrayList<Node>> graph = new ArrayList<ArrayList<Node>>();
  public static int[] distance = new int[30001];

  public static void dijkstra(int start) {
    PriorityQueue<Node> pq = new PriorityQueue<>();
    pq.offer(new Node(start, 0));
    distance[start] = 0;
    while (!pq.isEmpty()) {
      Node node = pq.poll();
      int dist = node.getDistance();
      int now = node.getIndex();
      if (distance[now] < dist) continue;
      for (int i = 0; i < graph.get(now).size(); i++) {
        int cost = distance[now] + graph.get(now).get(i).getDistance();
        if (cost < distance[graph.get(now).get(i).getIndex()]) {
          distance[graph.get(now).get(i).getIndex()] = cost;
          pq.offer(new Node(graph.get(now).get(i).getIndex(), cost));
        }
      }
    }
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    V = sc.nextInt();
    E = sc.nextInt();
    start = sc.nextInt();

    // 그래프 초기화
    for (int i = 0; i <= V; i++) {
      graph.add(new ArrayList<Node>());
    }

    // 모든 간선 정보를 입력받기
    for (int i = 0; i < E; i++) {
      int u = sc.nextInt();
      int v = sc.nextInt();
      int w = sc.nextInt();
      graph.get(u).add(new Node(v, w));
    }

    // 최단 거리 테이블 초기화
    Arrays.fill(distance, INF);

    dijkstra(start);

    for (int i = 1; i <= V; i++) {
      if (distance[i] == INF) {
        System.out.println("INF");
      } else {
        System.out.println(distance[i]);
      }
    }
  }
}
