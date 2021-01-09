from functools import lru_cache

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        nums.sort()
        
        @lru_cache(maxsize=None)
        def findMask(maxVal):
            mask = 1
            while mask <= maxVal:
                mask <<= 1
                if mask > maxVal:
                    break

                mask += 1
                
            return mask
        
        @lru_cache(maxsize=None)
        def take_closest(myNumber):
            nonlocal nums
            pos = bisect_left(nums, myNumber)
            if pos == 0:
                return nums[0]
            if pos == len(nums):
                return nums[-1]
            before = nums[pos - 1]
            after = nums[pos]
            if after == myNumber:
                return after
            return before

        
        @lru_cache(maxsize=None)
        def maxXOR(xi, mi):
            nonlocal nums
            
            iter = 0
            bestXOR = -1
            
            mask = findMask(max(mi,xi))
            idealXOR = xi ^ mask
            
            while idealXOR > mi:
                if idealXOR & 1:
                    idealXOR -= 1
                else:
                    idealXOR >>= 1
                
            print(idealXOR, mask, xi, mi)
            #find closest integer to idealXOR - lognm
            
            choice = take_closest(idealXOR)
            
            print(idealXOR, mask, xi, mi, choice)
            if choice <= mi:
                return xi ^ choice
            
            return bestXOR
            
        output = []
        
        for query in queries:
            output.append(maxXOR(query[0], query[1]))
            
        return output