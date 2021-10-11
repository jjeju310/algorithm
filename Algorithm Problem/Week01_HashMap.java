package AlgorithmProblem;

import java.util.HashMap;

// 프로그래머스 - 전화번호 목록 (https://programmers.co.kr/learn/courses/30/lessons/42577)
class Week01_HashMap {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        HashMap<String, Integer> phonebook = new HashMap<>();

        for(int i = 0; i < phone_book.length; i++) {
            phonebook.put(phone_book[i], i);
        }

        for(int i = 0; i < phone_book.length; i++) {
            for(int j = 1; j < phone_book[i].length(); j++) {
                if(phonebook.containsKey(phone_book[i].substring(0, j))) {
                    answer = false;
                    return answer;
                }
            }
        }
        
        return answer;
    }
}