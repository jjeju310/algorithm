package AlgorithmProblem;

import java.util.Comparator;
import java.util.PriorityQueue;

public class Week13_TreeHeap_redo {
  class Job {
    int reqTime; // 요청시점
    int runTime; // 처리시간

    public Job(int req, int run) {
      this.reqTime = req;
      this.runTime = run;
    }
  }

  public int solution(int[][] jobs) {
    // 대기큐: 작업 요청 시점이 빠른 순으로 정렬
    PriorityQueue<Job> queue = new PriorityQueue<>(new Comparator<Job>() {
      @Override
      public int compare(Job o1, Job o2) {
        return o1.reqTime - o2.reqTime;
      }
    });

    for(int[] job : jobs) {
      queue.add(new Job(job[0], job[1]));
    }

    // 작업큐: 작업 소요 시간이 빠른 순으로 정렬
    PriorityQueue<Job> taskQueue = new PriorityQueue<>(new Comparator<Job>() {
      @Override
      public int compare(Job o1, Job o2) {
        return o1.runTime - o2.runTime;
      }
    });

    int count = 0; // 작업 수
    int sum = 0;   // 요청 ~ 종료까지 걸린 시간의 합
    int time = 0;  // 처리시간

    while (count < jobs.length) {
      // 작업큐에 추가: 대기열이 비어있지 않고 요청시점이 됐을 때
      while (!queue.isEmpty() && time >= queue.peek().reqTime) {
        taskQueue.add(queue.poll());
      }

      // 작업큐에 작업이 있으면 우선순위에 따라 작업 진행
      if(!taskQueue.isEmpty()) {
        Job job = taskQueue.poll();
        sum += job.runTime + (time - job.reqTime);
        time += job.runTime;
        count++;
      } else { // 작업이 없으면 시간이 흐름
        time++;
      }
    }
    return sum / count; // 요청 ~ 종료 평균시간 리턴
  }
}
