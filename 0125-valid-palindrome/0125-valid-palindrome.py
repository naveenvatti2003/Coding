class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=s.lower()
        res=""
        for ele in n:
            if ele.isalnum():
                res+=ele
        rev=""
        for ele in res:
            rev=ele+rev
        return rev==res
        