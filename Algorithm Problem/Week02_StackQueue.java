package AlgorithmProblem;

import java.util.*;

// 프로그래머스 - 기능개발 (https://programmers.co.kr/learn/courses/30/lessons/42586)
public class Week02_StackQueue {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> queue = new LinkedList<>();

        for(int i = 0; i < progresses.length; i++) {
            queue.add((int)Math.ceil((100.0 - progresses[i]) / speeds[i]));
        }
        System.out.print(queue + " ");

        ArrayList<Integer> answer = new ArrayList<>();
        while (!queue.isEmpty()) {
            int leftDay = queue.poll();
            int count = 1;

            while (!queue.isEmpty() && leftDay >= queue.peek()) {
                count++;
                queue.poll();
            }
            answer.add(count);
        }
        System.out.print(answer + " ");

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
