class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []
        dp = [[None] * n for _ in range(n)]
        '''
        # Top down: Time O(N^4) Space O(N^2)
        def helper(l, r):
            if l == r: return [TreeNode(l+1)]
            if l > r: return [None]
            if dp[l][r] != None: return dp[l][r]
            dp[l][r] = []
            for i in range(l, r+1):
                for l_node in helper(l, i-1):
                    for r_node in helper(i+1, r):
                        dp[l][r].append(TreeNode(i+1, l_node, r_node))
            return dp[l][r]
        return helper(0, n-1)
        '''
        # Bottom up: Time O(N^4) Space O(N^2)
        #l is difference between left and right
        for l in range(1, n+1):
            #i is left
            for i in range(n+1-l):
                #why ? l == r?
                #r = i+l-1 
                if l == 1:
                    dp[i][i+l-1] = [TreeNode(i+1)]
                else:
                    dp[i][i+l-1] = []
                    #cand
                    for j in range(i, i+l):
                        #(l, r)
                        #why j-1 >= i ?
                        for l_node in dp[i][j-1] if j-1 >= i else [None]:
                            for r_node in dp[j+1][i+l-1] if j+1 <= i+l-1 else [None]:
                                dp[i][i+l-1].append(TreeNode(j+1, l_node, r_node))
        return dp[0][n-1]