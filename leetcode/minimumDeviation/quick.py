class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        maxv = max(nums)
        ans = float('inf')
        heapify(nums)
        while True:
            ans = min(ans, maxv - nums[0])
            if nums[0] % 2 == 1:
                v = heappop(nums)
                maxv = max(maxv, v * 2)
                heappush(nums, v * 2)
            else: break
        nums = [-n for n in nums]
        maxv = max(nums)
        heapify(nums)
        while True:
            ans = min(ans, maxv - nums[0])
            if nums[0] % 2 == 0:
                v = heappop(nums)
                maxv = max(maxv, v // 2)
                heappush(nums, v // 2)
            else: break
        return ans
                