from collections import deque
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ""
        
        #w1 = deque(word1)
        #w2 = deque(word2)
        
        w1iter = 0
        w2iter = 0
        
        while w1iter < len(word1) or w2iter < len(word2):
            
            if w1iter < len(word1) and w2iter < len(word2):
                
                if word1[w1iter] > word2[w2iter]:
                    merge += word1[w1iter]
                    w1iter += 1
                    
                elif word1[w1iter] < word2[w2iter]:
                    merge += word2[w2iter]
                    w2iter += 1
                    
                else:
                    if word1[w1iter:] > word2[w2iter:] :
                        merge += word1[w1iter]
                        w1iter += 1
                    else:
                        merge += word2[w2iter]
                        w2iter += 1
            elif w1iter < len(word1):
                merge += word1[w1iter]
                w1iter += 1
                
            else:
                merge += word2[w2iter]
                w2iter += 1
        
        """
        while len(w1) > 0 or len(w2) > 0:
            if len(w1) > 0 and len(w2) > 0:
                if w1[0] > w2[0]:
                    c = w1.popleft()
                    merge += c
                else:
                    c = w2.popleft()
                    merge += c
                    
            elif len(w1) > 0:
                c = w1.popleft()
                merge += c
                
            else:
                c = w2.popleft()
                merge += c
        """
        return merge