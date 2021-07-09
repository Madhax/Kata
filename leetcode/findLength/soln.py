class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        """
        @functools.cache
        def dp(i, j):
            
            if i == len(nums1) or j == len(nums2):
                return 0
            
            best = 0
            if nums1[i] == nums2[j]:
                best = max(best, 1 + dp(i+1, j+1))
                
            best = max(best, dp(i, j+1))
            best = max(best, dp(j+1, i))
            
            return best
        """
        
        dp = [[0 for _ in range(len(nums1)+1)] for _ in range(len(nums2)+1)]
        
        best = 0
        #dp[0][0] = nums1[0] == nums2[0]
        #dp[0][1] = nums1[0] == nums2[1]
        #dp[1][0] = nums1[1] == nums2[0]
        
        for i in range(0, len(nums2)):
            for j in range(0, len(nums1)):
                if nums2[i] == nums1[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                    #best = max(best, dp[i+1][j+1])
                else:
                    dp[i+1][j+1] = 0
                    
        
        return max(max(row) for row in dp)