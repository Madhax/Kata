class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ctr = 0
        for x in range(len(nums)):
            if nums[x] == 0:
                continue
            z = x + 2
            for y in range(x+1, len(nums)-1):
                while z < len(nums) and nums[x]+nums[y] > nums[z]:
                    z+=1
                    
                ctr += z-y-1
        return ctr
                