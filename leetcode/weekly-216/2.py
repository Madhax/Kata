class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        result = ['a'] * n
        
        def getValue(charList):
            result = 0
            for char in charList:
                result += ord(char) - ord('a') + 1
                
            return result
        
        iter = len(result) - 1
        k -= getValue(result)
        #print(getValue(result))
        while iter >= 0:
            if k > 25:
                result[iter] = 'z'
                k -= 25
                iter -= 1
                continue
            else:
                result[iter] = chr(ord('a') + k)
                return "".join(result)
        
            iter -= 1
        
        return ""