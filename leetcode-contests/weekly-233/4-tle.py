class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        nums.sort()
        numCtr = Counter()
        
        for num in nums:
            numCtr[num] += 1
            
        output = 0
        y = 0
        while y < len(nums):
            x = y + 1
            while x < len(nums):
                xorval = nums[y] ^ nums[x]
                if low <= xorval <= high:
                    output += numCtr[nums[y]] * numCtr[nums[x]]
                    
                x = bisect_left(nums, nums[x]+1)
                
            y = bisect_left(nums, nums[y]+1)
        
        return output