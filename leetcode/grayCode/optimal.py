class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0] 
        for i in range(0, n):
            peak = 2 ** i
            for j in range(peak - 1, -1, -1):
                res.append(peak ^ res[j]) 
        return res