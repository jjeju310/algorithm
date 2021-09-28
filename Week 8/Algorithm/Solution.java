import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        Arrays.sort(times);
        long start = times[0]; // �ּҽð�
        long end = (long)n * times[times.length - 1]; // �ִ�ð�

        while(start <= end) {
            long mid = (start + end) / 2; // �ɻ��ϴµ� �ɸ��� �ð��� �߰���
            long done = 0; // �ɻ������ �߰��ð��� �������� �ɻ��� �� �ִ� ��� ���� ��
            for(int i = 0; i < times.length; i++) {
                done = done + (mid/times[i]); // ��� �� = �־��� �ð�(mid) / �ذ� ������ �ð�
            }

            if(done < n) { // �ɻ縦 �ο���ŭ ���� ������ ��
                start = mid + 1;
            } else {
				answer = mid;
                end = mid - 1;                
            }
        }
        return answer;
    }
}