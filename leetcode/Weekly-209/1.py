class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(0, nums[-1] + 1):
            iter = 0
            while nums[iter] < x:
                iter += 1
                if iter == len(nums):
                    return -1
            
            if x == len(nums)-iter:
                return x
        
        return -1
        