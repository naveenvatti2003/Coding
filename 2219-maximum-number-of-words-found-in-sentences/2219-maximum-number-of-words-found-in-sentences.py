class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=0
        for i in sentences:
            temp=1
            for j in i:
                if(j==" "):
                    temp+=1
            ans=max(temp,ans)
        return ans

