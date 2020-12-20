from functools import lru_cache
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        @lru_cache(maxsize=None)
        def recurse(index):
            nonlocal nums, k
            
            if index < 0:
                return float("-inf")
            
            if index == 0:
                return nums[0]
            
            score = nums[index]
            
            mx = float("-inf")
            #for x in range(1, min(k+1, len(nums)-index-1)):
            #    if nums[index+x] < 0:
            #        continue
            slice = list(enumerate(nums[index-k-1:index-1].reverse()))
            
            
            slice.sort(key=lambda x: x[1], reverse=True)
            """
            for x in range(index-1, index-k-1, -1):
                #print(x)
                mx = max(mx, recurse(x))
            """
            print(slice)
            for x in range(min(5,len(slice))):
                mx = max(mx, recurse(index - (slice[x][0]+1)))
            return mx + score
            
        return recurse(len(nums)-1)