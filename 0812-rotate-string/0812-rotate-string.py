class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        temp=s
        res=""
        for i in range(len(temp)):
            temp=temp[1:]+temp[0]
            if temp==goal:
                res=temp
        if res:
            return True
        else:
            return False

        