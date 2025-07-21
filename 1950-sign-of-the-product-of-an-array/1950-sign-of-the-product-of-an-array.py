class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p=1
        for ele in nums:
            p*=ele
        if p>=1:
            return 1
        elif p==0:
            return 0
        else:
            return -1

        