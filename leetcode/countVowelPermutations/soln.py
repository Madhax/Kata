"""
Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
"""
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        #state = [[-1 for _ in range(20001)] for _ in range(5)]
        state = defaultdict(lambda: defaultdict(lambda:-1))
        #a e i o u
        paths = {0:[1], 1:[0,2], 2:[0,1,3,4],3:[2,4],4:[0]}
        
        
        def dfs(src, index):
            if index == 1:
                return 1
            
            if state[src][index] != -1:
                return state[src][index]
            
            ans = 0
            
            for opt in paths[src]:
                ans += dfs(opt, index-1)
                
            state[src][index] = ans
            return ans
        
        ans = 0
        for key in paths.keys():
            ans += dfs(key, n)
            
        return ans % ((10**9) + 7)
        #return dp('', n) % ((10**9) + 7)