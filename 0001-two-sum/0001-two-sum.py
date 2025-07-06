class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_a=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    list_a.extend([i,j])
                    break
        return list_a                    

        