package BasicJava;

import java.util.Scanner;

public class P015 {
    // 백준 1330
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num1 = sc.nextInt();
        int num2 = sc.nextInt();

        if(num1 > num2) {
            System.out.println(">");
        } else if(num1 < num2) {
            System.out.println("<");
        } else if(num1 == num2) {
            System.out.println("==");
        }
    }
}
