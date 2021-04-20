class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
       
        @functools.cache
        def recurse(target):
            if target == 0:
                return 1
            ans = 0
           
            for c in nums:
                if c > target:
                    break
                ans += recurse(target-c)
               
            return ans
       
        return recurse(target)

