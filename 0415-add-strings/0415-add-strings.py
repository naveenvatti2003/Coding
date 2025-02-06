class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        string1=int(num1)
        string2=int(num2)
        return str(string1+string2)       