class Solution:
    def solve(self, requests, k):
        mins = []
        maxs = []

        for start, end in requests:
            mins.append(start)
            maxs.append(end)

        mins.sort()
        maxs.sort()

        N = len(requests)

        ans = []
        for index, (start, end) in enumerate(requests):
            # the earliest this person can finish
            left = bisect.bisect_left(maxs, start)
            # the latest this person can finish (-1 for removing its own starting point)
            right = bisect.bisect_right(mins, end) - 1

            if left <= k <= right:
                ans.append(index)
        return ans
