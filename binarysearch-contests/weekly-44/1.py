class Solution:
    def solve(self, s):
        digits = "0123456789"
        curnum = ""
        output = 0
        for symbol in s:
            if symbol in digits:
                curnum += symbol
            else:
                if len(curnum) > 0:
                    output += int(curnum)
                    curnum = ""
                
        if len(curnum) > 0:
            output += int(curnum)
        return output
