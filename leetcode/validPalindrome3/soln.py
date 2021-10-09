class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        @functools.cache
        def dp(l, r):
            if l == r:
                return 1
            
            if l + 1 == r and s[l] == s[r]:
                return 2
            
            if s[l] == s[r]:
                return 2 + dp(l + 1, r - 1)
            
            return max(dp(l+1, r), dp(l, r-1))

            
        return dp(0, len(s)-1) >= len(s) - k
    
    