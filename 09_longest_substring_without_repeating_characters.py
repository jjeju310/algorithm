class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        dic = {}
        count_list = []
        count = 0
        i = 0
        while i < len(s):
            for n in range(i, len(s)):
                if s[n] not in dic:
                    dic[s[n]] = 1;
                    count += 1
                    #print("dic", dic)
                    #print("count!", count)
                else:
                    i += 1
                    count_list.append(count)
                    dic = {}
                    count = 0
                    break
                    
        #print(count_list)
        return(max(count_list) if len(count_list) != 0 else 0 )
        