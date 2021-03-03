class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        temp=set(nums)
        return [sum(nums)-sum(temp),(1+len(nums))*len(nums)//2-sum(temp)]