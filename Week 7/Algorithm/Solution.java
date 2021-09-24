package week7;

import java.util.*;

class Solution {
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