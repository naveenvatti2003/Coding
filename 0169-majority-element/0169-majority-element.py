class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        ans=-1
        temp=len(nums)//2
        for i in dic:
            val=dic[i]
            if val>temp:
                ans=i
                break
        return ans
