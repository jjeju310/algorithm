class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start_idx = 0
        used_chars = {}  #{"a":4, "b":2, "c":3}
        
        for idx, c in enumerate(s):  #ex. (0, a), (1,b), (2,c), (3,a)
            if c in used_chars: # 이미 등장했던 문자? (ex. a)
                start_idx = used_chars[c]+1 # start index 만 갱신
            
            else: # 앞에 없는 문자 (ex.b) 
                max_length = max(max_length, idx-start_idx+1) 
                # 두번째 루프라면 start 인덱스 뺀것까지가 길이 / 이거랑 원래 첫번째 루프의 max_length중에 큰거 비교
            
            used_chars[c]=idx # ex. {"a":"3"}
            
        return max_length