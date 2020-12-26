class Solution:
    def findDiagonalOrder(self, A):
        if not A:
            return []
        
        R, C = len(A), len(A[0])
    
        groups = [[] for _ in range(R + C)]
        
        for r in range(R):
            for c in range(C):
                groups[r + c].append(A[r][c])
                
                
        for r in range(0, R + C, 2):
            groups[r].reverse()
            
        return itertools.chain.from_iterable(groups)