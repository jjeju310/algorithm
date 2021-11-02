package AlgorithmProblem;

import java.util.LinkedList;
import java.util.Scanner;

public class Week11_LinkedList_redo {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int k = sc.nextInt();

    LinkedList<Integer> linkedList = new LinkedList<>();
    for(int i = 1; i <= n; i++) {
      linkedList.add(i);
    }

    System.out.print("<");

    while (!linkedList.isEmpty()) {
      for(int i = 0; i < k; i++) {
        if(i != (k-1)) {
          int index = linkedList.remove();
          linkedList.add(index);
        } else {
          int printIdx = linkedList.remove();
          if(linkedList.size() != 0) {
            System.out.print(printIdx + ", ");
          } else {
            System.out.print(printIdx);
          }
        }
      }
    }
    System.out.print(">");
  }
}
