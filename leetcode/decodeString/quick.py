class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        res = []
        
        for char in s:
            if char == ']':
                tmpStr = []
                k = 0
                base = 0
                while stack[-1] != '[':
                    tmpStr.append(stack.pop())
                stack.pop()
                while stack and stack[-1].isnumeric():
                    num = stack.pop()
                    k += (ord(num) - ord('0')) * (10 ** base)
                    base += 1
                for _ in range(k):
                    for i in range(len(tmpStr) - 1, -1, -1):
                        stack.append(tmpStr[i])
            else:
                stack.append(char)
        
        return  ''.join(stack)
    
        
                
