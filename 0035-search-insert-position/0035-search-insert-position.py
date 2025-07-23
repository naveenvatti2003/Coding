class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1]>=target:
            ans=-1
            l=0
            r=len(nums)-1
            while l<=r:
                m=(l+r)//2
                if nums[m]>=target:
                    ans=m
                    r=m-1 
                else:
                    l=m+1
            return ans
        else:
            return len(nums)