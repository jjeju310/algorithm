package BasicJava;

import java.util.Scanner;

public class P023 {
    // 백준 2742
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();
        for(int i = num; i > 0; i--) {
            System.out.println(i);
        }
    }
}
