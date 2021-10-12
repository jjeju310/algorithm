package AlgorithmProblem;

import java.util.*;

// 프로그래머스 - 구명보트 (https://programmers.co.kr/learn/courses/30/lessons/42885)
class Week08_Greedy {
    public int solution(int[] people, int limit) {
        Arrays.sort(people);
        int answer = 0;

        int min = 0;
        for(int max = people.length-1; min <= max; max--) {
            if(people[min] + people[max] > limit) {
                answer++;
            } else {
                answer++;
                min++;
            }
        }
        return answer;
    }
}
