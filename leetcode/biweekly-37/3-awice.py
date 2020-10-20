class Solution(object):
    def numberOfSets(self, N,K):
        MOD = 10 ** 9 + 7
        
        dp = [[0] * (K + 1) for _ in range(N)]
        dp[0][0] = 1
        for k in range(1, K + 1):
            s = 0
            for i in range(1, N):
                #dp[i][k] = sum(dp[i-j][k-1] * j for j in range(1, i + 1))
                s += dp[i - 1][k - 1]
                s %= MOD
                dp[i][k] = (dp[i-1][k] + s) %MOD
            
                
                
        return sum(row[-1] for row in dp) % MOD
