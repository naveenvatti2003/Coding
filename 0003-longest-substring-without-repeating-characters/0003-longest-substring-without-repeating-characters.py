class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=0
        for i in range(len(s)):
            res1=[]
            for j in range(i,len(s)):
                if s[j] not in res1:
                    res1.append(s[j])
                    max_length=max(max_length, len(res1))
                else:
                    break
        return max_length

              

                    

    
        
           