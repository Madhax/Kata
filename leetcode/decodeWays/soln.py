from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        mapping = {}
        
        for index, letter in enumerate(alphabet):
            #print(index, letter)
            mapping[str(index+1)] = letter
        
        
        @lru_cache(maxsize=None)
        def recurse(index):
            nonlocal s
            if index == len(s):
                return 1
            
            if index > len(s):
                return 0
            
            output = 0
            
            if s[index:index+1] in mapping:
                output += recurse(index+1)
            
            if s[index:index+2] in mapping:
                output += recurse(index+2)
                
            return output

        return recurse(0)