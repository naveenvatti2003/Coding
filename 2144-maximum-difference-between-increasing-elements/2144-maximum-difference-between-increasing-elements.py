class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        m=nums[0]
        ma=-1
        for i in range(1,len(nums)):
            if nums[i]>m:
                ma=max(ma,nums[i]-m)
            else:
                m=min(m,nums[i])
        return ma
     