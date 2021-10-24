package AlgorithmProblem;

import java.util.*;

// https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Week09_leetCode03_Hash {
  /*
   * 실패한 풀이
    public int lengthOfLongestSubstring(String s) {
      String result = "";

      for(int i = 0; i < s.length(); i++) {
        if(!result.contains(String.valueOf(s.charAt(i)))) {
          result += String.valueOf(s.charAt(i));
          System.out.println(result);
        }
      }
      return result.length();
  */

  private final Map<Character, Integer> indexMap = new HashMap<>();

  public int lengthOfLongestSubstring(String s) {
    int maxLength = 0;
    int startIndex = 0; // substring을 시작할 문자의 인덱스 지정
    for (int i = 0; i < s.length(); i++) {
      char tempChar = s.charAt(i);
      if (indexMap.containsKey(tempChar) && indexMap.get(tempChar) >= startIndex) { // 문자가 이미 등장했거나 시작 인덱스보다 크거나 같을 때
        maxLength = Math.max(maxLength, i - startIndex); // 최대길이 갱신
        startIndex = indexMap.get(tempChar) + 1; // 시작 인덱스 1 증가
      }
      indexMap.put(tempChar, i);
    }
    return Math.max(maxLength, s.length() - startIndex);
  }
}