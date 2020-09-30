class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.helper(nums, 3, target)
    
    def helper(self, nums, k, target):
        if k == len(nums):
            return sum(nums)
        curr = sum(nums[:k])
        if curr >= target:
            return curr
        curr = sum(nums[-k:])
        if curr <= target:
            return curr
        if k == 1:
            return min([(x, abs(target -x)) for x in nums], key = lambda x: x[1])[0]
        closest = sum(nums[:k])
        for i, x in enumerate(nums[:-k+1]):
            if i > 0 and x == nums[i-1]:
                continue
            curr = self.helper(nums[i+1:], k-1, target-x) + x
            if(abs(target-curr) < abs(target-closest)):
                if target == curr:
                    return target
                else:
                    closest = curr
        return closest