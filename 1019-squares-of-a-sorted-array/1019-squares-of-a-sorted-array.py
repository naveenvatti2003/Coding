class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        list_a=[]
        for ele in nums:
            list_a.append(ele*ele)
        list_a.sort()
        return list_a

        
        