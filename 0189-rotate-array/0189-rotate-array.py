class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        m=k%len(nums)
        nums[:]=nums[-m:]+nums[:-m]
        return nums    