class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def nSum(target, nums, n, prep):
            res = set()
            seen = set()
            if n > len(nums):
                return set()
            if n == 2:
                for num in nums:
                    if target-num in seen:
                        res.add(tuple(prep + [num, target-num]))
                    
                    seen.add(num)
                return res
            else:
                i = 0
                res = set()
                while i < len(nums):
                    if nums[i]*n > target or nums[-1]*n < target:
                        break
                    elif i-1>=0 and nums[i] == nums[i-1]:
                        i+=1
                    else:
                        res |= nSum(target-nums[i], nums[i+1:], n-1, prep + [nums[i]])
                        print(res)
                        i += 1
                return res
            
        nums.sort()
        return nSum(target, nums, 4, [])
                                    