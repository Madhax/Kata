class Solution:
        
    def numDecodings(self, s: str) -> int:

#         start:f(n) = 0
#         if last one digits not 0, f(n) = f(n) + f(n-1)
#         if last two digits within [10~26], f(n) = f(n)+f(n-2)

        length = len(s)
        
#         length 0 case:
        if length == 0: 
            return 0
#         length 1 case:
        if length == 1: 
            if s[0]=="0": 
                return 0
            else:
                return 1
            
#         now we assume length>=2:
        
        pos0 = 0
        pos1 = 1
        
        num0 = 1
        num1 = 0
        
#         initialize num1:
        if s[0]=="0":
            return 0
        else:
            num1 = 1
        
            
        for i in range(2,length+1):
            num = 0
            if s[i-1]!="0":
                num = num + num1
            if int(s[i-2:i])<=26 and int(s[i-2:i])>=10:
                num = num + num0
            
            num0, num1 = num1, num
                
            
        
        
        
        return num1