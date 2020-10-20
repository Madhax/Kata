import functools
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
       
        @lru_cache(maxsize=None)
        def doesMatch(s, index, pattern, patternIndex):
            #print(index, patternIndex)
            result = False
            sLen = len(s)
           
            if index > sLen:
                return False
           
            if index == sLen:
                if patternIndex == len(pattern):
                    return True
               
            if len(pattern) <= patternIndex:
                return False
           
            if pattern[patternIndex] == "?":
                #match single character
                result |= doesMatch(s, index+1, pattern, patternIndex+1)
            elif pattern[patternIndex] == "*":
                #match one or more characters
                result |= doesMatch(s, index+1, pattern, patternIndex)
                result |= doesMatch(s, index+1, pattern, patternIndex+1)
                result |= doesMatch(s, index, pattern, patternIndex+1)
               
            elif index < sLen and pattern[patternIndex] == s[index]:
                #character matches
                result |= doesMatch(s, index+1, pattern, patternIndex+1)
            else:
                return False
           
            return result
       
        return doesMatch(s, 0, p, 0)
