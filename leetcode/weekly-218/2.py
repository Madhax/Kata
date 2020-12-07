class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        found = 0 
        l = 0
        r = len(nums) - 1
        
        while True:
            val = nums[l] + nums[r]
                
            if r <= l or r < 0 or l >= len(nums):
                break
                
            if nums[l] + nums[r] == k:
                found += 1
                l += 1
                r -= 1
                continue
                
            if val > k:
                r -= 1
                continue
                
            if val < k:
                l += 1
                continue
            
        return found