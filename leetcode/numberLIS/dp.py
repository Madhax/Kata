from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        resLength = 1
        resCount = 1

        dp = [{'length': 1, 'count': 1}] * len(nums)
        for i in range(1, len(nums)):
            curMax = 1
            curList = []
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                newLength = dp[j]['length'] + 1
                if newLength > curMax:
                    curMax = newLength
                    curList = [j]
                elif newLength == curMax:
                    curList.append(j)

            if len(curList) > 0:
                dp[i] = {
                    'length': curMax,
                    'count': sum([dp[j]['count'] for j in curList]),
                }

            if dp[i]['length'] == resLength:
                resCount += dp[i]['count']
            elif dp[i]['length'] > resLength:
                resLength = dp[i]['length']
                resCount = dp[i]['count']

        return resCount 