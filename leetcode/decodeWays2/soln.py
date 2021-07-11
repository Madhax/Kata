class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = (10**9) + 7
        
        @functools.cache
        
        def decodeWays(parent, index):
            if index == len(s):
                if parent == None:
                    return 1
                else:
                    return 0
            
    
            numWays = 0
        
            if parent == None:
    
                if s[index] == '*':
                    #no parent 
                    numWays += 9 * decodeWays(None, index+1)
                    #choose 1
                    numWays += decodeWays(1, index+1)
                    #choose 2
                    numWays += decodeWays(2, index+1)
                    
                
                if s[index] == '1':
                    numWays += decodeWays(1, index+1)
                    
                if s[index] == '2':
                    numWays += decodeWays(2, index+1)
                    
                if '1' <= s[index] <= '9':
                    numWays += decodeWays(None, index+1)
                    
                    
            if parent == 1:
                if s[index] == '*':
                    numWays += 9 * decodeWays(None, index+1)
                    
                else:
                    numWays += decodeWays(None, index+1)
                    
            
            if parent == 2:
                if s[index] == '*':
                    numWays += 6 * decodeWays(None, index+1)
                elif s[index] > '6':
                    return 0
                else:
                    numWays += decodeWays(None, index+1)
                    
            
            
        
            return numWays % MOD
        
        
        return decodeWays(None, 0) % MOD