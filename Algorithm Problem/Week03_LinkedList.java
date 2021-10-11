package AlgorithmProblem;

import java.util.LinkedList;
import java.util.Scanner;

// 백준 1158 - 요세푸스 문제 (https://www.acmicpc.net/problem/1158)
public class Week03_LinkedList {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LinkedList<Integer> list = new LinkedList<>();
        int n = sc.nextInt(); // 사람수
        int k = sc.nextInt(); // 제거할 k번째 순서
        int i, j;

        for(i=1; i<=n; i++) {
            list.add(i);
        }

        System.out.print("<");

        while (!list.isEmpty()) {
            for(j=0; j<k; j++) {
                if(j==(k-1)) {
                    int number = list.remove();
                    if (list.size()!=0) {
                        System.out.print(number + ", ");
                    } else {
                        System.out.print(number);
                    }
                } else {
                    list.add(list.remove());
                }
            }
        }

        System.out.print(">");

    }
}
