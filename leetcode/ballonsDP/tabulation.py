class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [n for n in nums if n] + [1]
        n = len(nums)
        dp =[[0]*n for _ in range(n)]
        for l in range(2, n):
            for left in range(n-l):
                right = left + l
                dp[left][right] = max(nums[left]*nums[k]*nums[right] + dp[left][k] + dp[k][right] for k in range(left+1, right))
        return dp[0][-1]
    