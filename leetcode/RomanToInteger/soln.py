class Solution:
    def romanToInt(self, s: str) -> int:
        iter = 0
        num = 0
        while iter < len(s):
            if s[iter:iter+1] == "M":
                num += 1000
                iter += 1
            elif s[iter:iter+2] == "CM":
                num += 900
                iter += 2
            elif s[iter:iter+1] == "D":
                num += 500
                iter += 1
            elif s[iter:iter+2] == "CD":
                num += 400
                iter += 2
            elif s[iter:iter+1] == "C":
                num += 100
                iter += 1
            elif s[iter:iter+2] == "XC":
                num += 90
                iter += 2
            elif s[iter:iter+1] == "L":
                num += 50
                iter += 1
            elif s[iter:iter+2] == "XL":
                num += 40
                iter += 2
            elif s[iter:iter+1] == "X":
                num += 10
                iter += 1
            elif s[iter:iter+2] == "IX":
                num += 9
                iter += 2
            elif s[iter:iter+1] == "V":
                num += 5
                iter += 1
            elif s[iter:iter+2] == "IV":
                num += 4
                iter += 2
            elif s[iter:iter+1] == "I":
                num += 1
                iter += 1
        return num
                