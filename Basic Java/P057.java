package BasicJava;

import java.util.Scanner;

// 백준 2869
public class P057 {
  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    int up = in.nextInt();		// A
    int down = in.nextInt();	// B
    int length = in.nextInt(); 	// C

    int day = (length - down) / (up - down);

    // 나머지가 있을 경우 (잔여 블럭이 있을 경우)
    if ((length - down) % (up - down) != 0) {
      day++;
    }
    System.out.println(day);
  }
}
