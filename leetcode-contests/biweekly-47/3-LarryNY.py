class Solution:
    def beautySum(self, s: str) -> int:
        N = len(s)
        ans = 0
        
        for start in range(N):
            f = [0] * 26
            mx = 0
            mn = 0
            
            for end in range(start, N):
                c = ord(s[end]) - ord('a')
                
                f[c] += 1
                if f[c] > mx:
                    mx = f[c]
                    
                mn = min(x for x in f if x > 0)
                ans += mx - mn
        return ans