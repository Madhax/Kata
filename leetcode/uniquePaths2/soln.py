class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        N = len(obstacleGrid)
        M = len(obstacleGrid[0])
        
        @functools.cache
        def dp(i, j):
            
            if i == N-1 and j == M-1:
                return 1
            
            paths = 0
            
            for path in [[1,0],[0,1]]:
                if 0 <= i + path[0] < N and 0 <= j + path[1] < M and obstacleGrid[i+path[0]][j+path[1]] == 0:
                    paths += dp(i+path[0], j+path[1]) 
                    
            return paths
        if obstacleGrid[0][0] == 1:
            return 0
        return dp(0,0)