class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        maxDiff = len(nums) - 1
        nums.sort()
        #print(nums)
        bestRange = 0
        
        work = deque()

        idx = 1
        work.append(nums[0])
        dups = Counter()
        dups[nums[0]] += 1
        curDups = 0
        while idx < len(nums):
                
            while idx < len(nums) and nums[idx] - work[0] <= maxDiff:
                work.append(nums[idx])
                dups[nums[idx]] += 1
                if dups[nums[idx]] > 1:
                    curDups += 1
                
                idx += 1
                
            bestRange = max(bestRange, len(work)-curDups)    
            while idx < len(nums) and work and nums[idx] - work[0] > maxDiff:
                val = work.popleft()
                dups[val] -= 1
                if dups[val] >= 1:
                    curDups -= 1
                
            if not work:
                work.append(nums[idx])
                dups[nums[idx]] += 1
                idx += 1
            
        return len(nums) - bestRange 
