class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=0
        for ele in nums:
           c=nums.count(ele)
           if c==1:
            return ele