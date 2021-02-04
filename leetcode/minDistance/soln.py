class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = list(word1)
        word2 = list(word2)
       
        @functools.cache
        def dp(y,x):
            nonlocal word1, word2
            #print(y,x)
            operations = math.inf
           
            if y == len(word1) and x == len(word2):
                return 0
           
            #insert
            if y == len(word1):
                return 1 + dp(y, x+1)
                #return math.inf
           
            #delete
            if x == len(word2):
                return 1 + dp(y+1, x)
           
            if word1[y] == word2[x]:
                operations = min(operations, dp(y+1, x+1))
               
            #delete
            operations = min(operations, 1 + dp(y+1, x))
           
            #replace
            operations = min(operations, 1 + dp(y+1, x+1))
           
            #insert
            operations = min(operations, 1 + dp(y, x+1))
           
            return operations
       
       
       
        return dp(0, 0)