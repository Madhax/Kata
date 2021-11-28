class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = 0
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if abs(nums[x] - nums[y]) == k:
                    cnt += 1
                    
        return cnt