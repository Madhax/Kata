class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        newnums = nums.copy()
        newnums.sort()
        
        #print(nums, newnums)
        i = 0
        while  i < N and newnums[i] == nums[i]:
            i += 1
        
        if i == N:
            return 0
        
        j = len(nums) - 1
        while j >= 0 and newnums[j] == nums[j]:
            j -= 1
            
        return max(j - i + 1, 0)