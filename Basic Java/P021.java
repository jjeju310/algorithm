package BasicJava;

import java.util.Scanner;

public class P021 {
    // 백준 8393
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();
        int sum = 0;

        for(int i = 1; i <= num; i++) {
            sum = sum + i;
        }
        System.out.println(sum);
    }
}
