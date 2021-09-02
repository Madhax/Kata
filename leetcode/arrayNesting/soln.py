class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        N = len(nums)
        seen = [False] * N
        best = 0
        
        for x in range(N):
            if seen[x]:
                continue
            cnt = 0
            while not seen[x]:
                seen[x] = True
                x = nums[x]
                cnt += 1
            best = max(cnt, best)
                
        return best