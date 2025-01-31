class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
       ans=-1
       list_length=len(nums)
       for i in range(list_length):
        for j in range(i+1,list_length):
            if(nums[i]<nums[j]):
                ans=max(ans,nums[j]-nums[i])
       return ans
