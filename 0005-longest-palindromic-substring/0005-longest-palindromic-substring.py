class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length=""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                res=s[i:j]
                if res==res[::-1] and len(res)>=len(max_length):
                    max_length=res
        return max_length
        