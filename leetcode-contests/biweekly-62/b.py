class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        cnt = 0
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if nums[x]+nums[y] == target:
                    cnt += 1
                if nums[y]+nums[x] == target:
                    cnt += 1
                    
        return cnt