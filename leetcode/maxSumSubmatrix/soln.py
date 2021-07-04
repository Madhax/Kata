class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:

        # For corner cases
        if not matrix:
            return 0
        
        def max_sumk(l, k):
            sums = [0]
            presum, ans = 0, -sys.maxsize
            for item in l:
                presum += item
                
                left = bisect.bisect_left(sums, presum - k)
                if left < len(sums):
                    ans = max(ans, presum - sums[left])
                    
                bisect.insort(sums, presum)
            return ans

        
        
        rows = len(matrix)
        cols = len(matrix[0])
        ans = -sys.maxsize
       
        # iterating through all  2D arrays possible for every column. 
        for i in range(cols):
            Cvalues = [0 for _ in range(rows)]
            
            for j in range(i, cols):
                
                for row in range(rows):
                    Cvalues[row] = Cvalues[row] + matrix[row][j]
                
                curr_sum = max_sumk(Cvalues, k)
                ans = max(curr_sum, ans)
        
        return ans