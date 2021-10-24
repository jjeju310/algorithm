package BasicJava;

import java.util.Scanner;
import java.util.StringTokenizer;

// 백준 1152
public class P049 {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    String S = in.nextLine();
    in.close();

    // st 에 공백을 기준으로 나눈 토큰들을 st 에 저장한다
    StringTokenizer st = new StringTokenizer(S," ");

    // countTokens() 는 토큰의 개수를 반환한다
    System.out.println(st.countTokens());

  }
}
