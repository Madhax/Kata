class Solution:
    def findIntegers(self, num):
        s = bin(num + 1)[2:]
        n = len(s)
        dp = [1, 2] + [0]*(n-2)
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        flag, ans = 0, 0
        for i in range(n):
            if s[i] == "0": continue
            if flag == 1: break
            if i > 0 and s[i-1] == "1": flag = 1
            ans += dp[-i-1]
        
        return ans