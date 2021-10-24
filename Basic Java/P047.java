package BasicJava;

import java.util.Scanner;

// 백준 2675
public class P047 {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    int T = in.nextInt();
    for(int i = 0; i < T; i++) {

      int R = in.nextInt();
      String S = in.next();	// nextLine() 을 쓰면 error!

      for(int j = 0; j < S.length(); j++) {
        for(int k = 0; k < R; k++) {	// R 만큼 반복 출력
          System.out.print(S.charAt(j));
        }
      }

      System.out.println();
    }
  }
}
