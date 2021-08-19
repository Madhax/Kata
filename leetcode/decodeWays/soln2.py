class Solution:
    def numDecodings(self, s: str) -> int:
        valid = set()
        for x in range(1, 27):
            valid.add(str(x))
            
        @functools.cache
        def dp(index, isSecond):
            if index == len(s):
                if isSecond:
                    return (False, 0)
                return (True, 1)
            
            cnt = 0
            isValid = False
            if isSecond:
                cand = s[index-1] + s[index]
                if cand not in valid:
                    return (False, 0)
                
                ret = dp(index+1, False)
                if ret[0]:
                    cnt += ret[1]
                    isValid = True
                #cnt = 1 + dp(index+1, False)
            else:
                if s[index] in valid:
                    ret = dp(index+1, False)
                    if ret[0]:
                        cnt += ret[1]
                        isValid = True
                    #cnt += 1 + 
                
                ret = dp(index+1, True)
                if ret[0]:
                    cnt += ret[1]
                    isValid = True
                #cnt += dp(index+1, True)
                
            return (isValid, cnt)
        
        ret = dp(0, False)
        if ret[0]:
            return ret[1]
        return 0
        #return dp(0, False)[1]