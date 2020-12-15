class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        
        dp = {0:[[]], 1:[[s[0]]]}
        
        for i in range(1, len(s)):
            dp[i+1] = []
            
            for j in range(0, i+1):
                if self.is_palindrome(s[j:i+1]):
                    for prev in dp[j]:
                        dp[i+1].append(prev + [s[j:i+1]])
        
        return dp[len(s)]
                
    
    def is_palindrome(self, s):
        return s == s[::-1]