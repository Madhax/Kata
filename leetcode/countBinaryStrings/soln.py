class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        ones = 0
        zeroes = 0
        
        cnt = 0 
        
        if s[0] == "0":
            zeroes += 1
        else:
            ones += 1
            
        for x in range(1, len(s)):
            if s[x] == s[x-1]:
                if s[x] == "0":
                    zeroes += 1
                else:
                    ones += 1
            
            else:
                mult = min(zeroes, ones)
                cnt += mult
                #print(x, cnt)
                if s[x] == "0":
                    zeroes = 1
                else:
                    ones = 1
                    
        mult = min(zeroes, ones)
        cnt += mult
        return cnt
    