package AlgorithmProblem;

import java.util.*;

// 프로그래머스 - 입국심사 (https://programmers.co.kr/learn/courses/30/lessons/43238)
class Week07_BinarySearch {
    public long solution(int n, int[] times) {
        long answer = 0;
        Arrays.sort(times);
        long start = times[0]; // 최소시간
        long end = (long)n * times[times.length - 1]; // 최대시간

        while(start <= end) {
            long mid = (start + end) / 2; // 심사하는데 걸리는 시간의 중간값
            long done = 0; // 심사관마다 중간시간을 기준으로 심사할 수 있는 사람 수의 합
            for(int i = 0; i < times.length; i++) {
                done = done + (mid/times[i]); // 사람 수 = 주어진 시간(mid) / 해결 가능한 시간
            }

            if(done < n) { // 심사를 인원만큼 하지 못했을 때
                start = mid + 1;
            } else {
                answer = mid;
                end = mid - 1;
            }
        }
        return answer;
    }
}