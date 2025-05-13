class Solution:
    def reverseDegree(self, s: str) -> int:
        ans, id = 0, 1
        for char in s:
            ans+=(123-ord(char))*id
            id+=1
        return ans
        