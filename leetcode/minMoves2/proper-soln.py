class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        middle_element = nums[len(nums)//2]        
        for num in nums:
            count += abs(middle_element - num)     
        return count