class Solution:
    def sortSentence(self, s: str) -> str:
        res=""
        s1=s.split()
        for i in range(len(s1)):
            m=i
            for j in range(i+1,len(s1)):
                if s1[j][-1]<s1[m][-1]:
                    m=j
            s1[i],s1[m]=s1[m],s1[i]
        for ele in s1:
            res+=str(ele[:-1])+" "
        return res.strip()


        
        