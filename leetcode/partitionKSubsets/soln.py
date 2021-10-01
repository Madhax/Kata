class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        sub_total = total // k
        n = len(nums)
        visited = [False] * len(nums)
        nums.sort(reverse=True)

        def backTracking(idx: int, g: int, t: int) -> bool:
			# break point
            if g > k:
                return True
            for i in range(idx, n):
                if visited[i] or nums[i] > t:
                    continue
                t -= nums[i]
                visited[i] = True
                if t == 0:
					# continue find elements for (g+1) th subset
                    if backTracking(0, g + 1, sub_total):
                        return True
                else:
					# continue find next element for g th subset
                    if backTracking(i+1, g, t):
                        return True
				# the back point
                visited[i] = False
                t += nums[i]
            return False

        return backTracking(0, 1, sub_total)
        
        