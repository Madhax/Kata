class Solution:
    def longestValidParentheses(self, s: str) -> int:
        x = 0
        maxLength = 0
        counter = 0
        currentLength = 0
        while x < len(s):
            currentLength += 1
            if s[x] == "(":
                counter += 1
            elif s[x] == ")":
                counter -= 1
               
            if counter == 0:
                if maxLength < currentLength:
                    maxLength = currentLength
                   
            if counter < 0:
                currentLength = 0
                counter = 0
               
            x += 1
           
        x = len(s) - 1
        currentLength = 0
        counter = 0
        while x > -1:
            currentLength += 1
            if s[x] == "(":
                counter += 1
            elif s[x] == ")":
                counter -= 1
               
            if counter == 0:
                if maxLength < currentLength:
                    maxLength = currentLength
                   
            if counter > 0:
                currentLength = 0
                counter = 0
               
            x -= 1
       
        return maxLength
