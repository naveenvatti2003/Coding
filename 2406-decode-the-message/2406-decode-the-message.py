class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dic={}
        temp=97
        for val in key:
            if (val!=" ") and (val not in dic):
                dic[val]=chr(temp)
                temp+=1
        string=""
        for val in message:
            if val==" ":
                string+=" "
            else:
                string+=dic[val]
        return string


        