class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        if nums[0] < 0:
            nums = [x+abs(nums[0]) for x in nums]
            
        start = 0
        prefixSum = []
        for x in nums:
            start += x
            prefixSum.append(start)
        
        memo=set()
        best = math.inf
        #print(prefixSum)
        for x in range(len(nums)):
            if nums[x] in memo:
                continue
            
            val = nums[x]
            
            cost = 0
            if x > 0:
                cost += (val*(x+1)) - (prefixSum[x-1])
            if x < N-1:
                if x == 0:
                    cost += ((prefixSum[N-1] - prefixSum[x]) - (val * ((N-1)-x)))
                else:
                    cost += ((prefixSum[N-1] - prefixSum[x]) - (val * ((N)-x)))
            
            #print(x, cost)
            best = min(best, cost)
            
            
        return best