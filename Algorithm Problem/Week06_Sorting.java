package AlgorithmProblem;

import java.util.*;

// 프로그래머스 - H-Index (https://programmers.co.kr/learn/courses/30/lessons/42747)
class Week06_Sorting {
    public int solution(int[] citations) {
        int answer = 0;
        // 0 1 3 5 6
        Arrays.sort(citations);
        
        for(int i = 0; i < citations.length; i++) {
            int h = citations.length-i;
            if(citations[i] >= h) {
                answer = h;
                break;
            }
        }
        
        return answer;
    }
}