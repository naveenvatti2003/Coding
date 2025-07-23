class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans=-1
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                ans=m
                return ans
            elif nums[m]<target:
                l=m+1 
            else:
                r=m-1
        return ans

        