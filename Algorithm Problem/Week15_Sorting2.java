package AlgorithmProblem;

import java.util.Arrays;
import java.util.Comparator;

// 프로그래머스 - 파일명 정렬(https://programmers.co.kr/learn/courses/30/lessons/17686)
public class Week15_Sorting2 {
  public String[] solution(String[] files) {
    String[] answer = {};
    Arrays.sort(files, new Comparator<String>() {
      @Override
      public int compare(String o1, String o2) {
        String head1 = o1.split("[0-9]")[0];
        String head2 = o2.split("[0-9]")[0];

        int result = head1.toLowerCase().compareTo(head2.toLowerCase());

        if(result == 0) {
          result = compareNum(o1, head1) - compareNum(o2, head2);
        }
        return result;
      }
    });

    return files;
  }

  public int compareNum(String string, String head) {
    string = string.substring(head.length()); // head의 길이만큼 잘라서 숫자부터 시작하도록 만듦
    String result = "";
    for(char c : string.toCharArray()) {
      if(Character.isDigit(c) && result.length() < 5) { // 숫자인지, result 길이가 5가 넘지 않는지 확인
        result += c;
      } else {
        break;
      }
    }
    return Integer.valueOf(result);
  }
}
