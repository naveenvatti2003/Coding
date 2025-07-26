class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        list_a=[]
        for i in words:
            res=i.split(separator)
            for word in res:
                if word:
                    list_a.append(word)
        return list_a
     
     
        
            