class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)
        ans=0
        for i in range(n):
            if(colors[i]!=colors[n-1]):
                temp=n-1-i
                ans=max(temp,ans)
        for i in range(n-1,-1,-1):
            if(colors[i]!=colors[0]):
                temp=i
                ans=max(temp,ans)
        return ans
        