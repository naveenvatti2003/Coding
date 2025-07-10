class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ma_cou=0
        co=0
        for i in range(len(nums)):
            if nums[i]==1:
                co+=1
                if co>ma_cou:
                    ma_cou=co
            else:
                co=0
        return ma_cou
        
        