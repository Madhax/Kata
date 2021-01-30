class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        output = ['a'] * n
        k -= n
        #print(output)
        iter = len(output) - 1
        while k > 0:
            #print(k)
            if k > 25:
                output[iter] = chr(ord('a') + 25)
                k -= 25
                iter -= 1
            else:
                output[iter] = chr(ord('a') + k)
                k = 0
        
        return "".join(output)