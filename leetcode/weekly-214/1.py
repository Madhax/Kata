class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0]*101
        if n == 0:
            return 0
        if n == 1:
            return 1
        nums[0] = 0
        nums[1] = 1
        for x in range(2, n+1):
            offset = x
            if x % 2 > 0:
                offset -= 1
                offset /= 2
                nums[x] = nums[int(offset)] + nums[int(offset) + 1]
            else:
                offset /= 2
                nums[x] = nums[int(offset)]
                
        
        return max(nums)
