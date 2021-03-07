#copy
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = [word[::-1] for word in words]
        words = sorted(words)

        N = len(words)
        n_total = 0
        for i in range(1,N):
            prev = words[i-1]
            n_prev = len(prev)
            
            if words[i][:n_prev]!=prev:
                n_total+=(n_prev+1)
                

        n_total+=(len(words[-1])+1)
        
                
        return n_total