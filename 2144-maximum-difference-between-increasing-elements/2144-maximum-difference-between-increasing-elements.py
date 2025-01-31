class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
       ans=-1
       low=nums[0]
       for i in range(1,len(nums)):
        if(low<nums[i]):
            ans=max(ans,nums[i]-low)
        low=min(low,nums[i])
       return ans
    
