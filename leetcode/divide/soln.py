class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX = 2 ** 31 - 1
        if dividend == 0:
            return 0

        if dividend < 0 and divisor < 0:
            sign = 1
        elif dividend < 0 or divisor < 0:
            sign = -1
        else:
            sign = 1
            
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        
        ret = 0
        while dividend > (divisor+divisor):
            highdivisor = divisor
            retadder = 1
            while True:
                if highdivisor + divisor > dividend:
                    break

                dividend -= highdivisor
                highdivisor += divisor
                ret += retadder
                retadder += 1
           
        #(dividend, highdivisor, retadder, ret, divisor)
        
        while dividend >= divisor:
            dividend -= divisor
            ret += 1

        if sign < 0:
            ret = -ret

        return min(int(ret),(2**31 - 1))