class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        totalSum = sum(nums)
        
        if totalSum % 2 != 0: 
            return False
        
        self.subsetSum = totalSum // 2
        self.memo = {}
        self.nums = nums
        self.nums.sort(reverse=True)
        
        return self.backtrack(2, 0, 0)

    def backtrack(self, k, idx, curr):
        if k == 1:
            return True
        if curr == self.subsetSum:
            return self.backtrack(k-1, 0, 0)
        for i in range(idx, len(self.nums)):
            if not i in self.memo and curr+self.nums[i] <= self.subsetSum:
                self.memo[i] = True
                if self.backtrack(k, i+1, curr+self.nums[i]):
                    return True
                self.memo[i] = False
                
        return False