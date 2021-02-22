class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        N1 = len(word1)
        N2 = len(word2)
        
        word = word1 + word2
        N = len(word)
        word2 = "".join(reversed(list(word2)))
        
        @lru_cache(None)
        def go(left, right):
            if left == right:
                return 1
            if left > right:
                return 0
            
            best = 0
            
            if word[left] == word[right]:
                best = max(go(left + 1, right - 1) + 2, best)
            best = max(go(left + 1, right), best)
            best = max(go(left, right - 1), best)
            
            return best
            
        
        best = 0
        for i in range(N1):
            for j in range(N2):
                if word1[i] == word2[j]:
                    best = max(best, go(i + 1, N - j - 1 - 1) + 2)
                    #print(i, j, go(i + 1, N - j - 1 - 1) + 2)
        return best