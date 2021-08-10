class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        def strtoint(s):
            val = 0
            for c in s:
                #print(c)
                val += ord(c) - ord('0')
                val *= 10
                
            #print(val)
            val //= 10
            #print(val)
            return val
        
        def inttostr(i):
            ret = []
            while i:
                ret.append(chr(int(ord('0') + (i % 10))))
                i //= 10
                
            return "".join(reversed(ret))
        
        ret = inttostr(strtoint(num1) + strtoint(num2))
        if ret:
            return ret
        return "0"
            
                
                