class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        
        iter = 0
        while iter < len(word1) or iter < len(word2):
            if iter < len(word1):
                output += word1[iter]
            if iter < len(word2):
                output += word2[iter]
                
            iter += 1
            
        return output