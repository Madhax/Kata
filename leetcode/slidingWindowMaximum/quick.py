class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        m = max(nums[:k])
        res = [m]
        left = 0
        for n in range(k, len(nums)):
            cur = nums[n]
            left += 1
            if left > 0 and nums[left - 1] == m:
                if nums[left] == m - 1:
                    m = nums[left]
                else:
                    m = max(nums[left: n + 1])
            if cur > m:
                m = cur
            res.append(m)
        return res