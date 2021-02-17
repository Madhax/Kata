class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        results = [S]
        
        for i in range(len(S)):
            c = S[i]
            
            if '0' <= c <= '9':
                continue
                
            n = len(results)
            for j in range(n):
                s = results[j]
                
                if 'a' <= c <= 'z':
                    new_C = c.upper()
                else:
                    new_C = c.lower()
                    
                results.append(s[:i] + new_C + s[i+1:])
                
        return results