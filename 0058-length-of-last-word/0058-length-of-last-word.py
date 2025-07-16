class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        m=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":
                m+=len(s[i])
            else:
                break
        return m

        