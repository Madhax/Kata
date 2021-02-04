class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: 
            return 0
        
        nums = [int("".join(row), base = 2) for row in matrix]
        ans = 0
        for i in range(len(nums)):
            cur = -1
            for j in range(i, len(nums)):
                cur &= nums[j]
                if cur == 0: 
                    break
                cnt = 0
                tmp = cur
                while tmp:
                    cnt += 1
                    tmp &= tmp >> 1
                area = cnt * (j - i + 1)
                if area > ans: 
                    ans = area
        return ans