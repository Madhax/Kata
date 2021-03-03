class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        opt = [0]*len(triangle[-1])
        opt[0] = triangle[0][0]
        
        for row in range(1, len(triangle)):
            level = triangle[row]
            
            for col in range(len(level)-1, -1, -1):
                val = level[col]
                
                if col == len(level)-1:
                    opt[col] = val + opt[col-1]
                elif col == 0:
                    opt[col] += val
                else:
                    opt[col] = min(opt[col], opt[col-1]) + val
                
        return min(opt)