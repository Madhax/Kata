class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = int(dividend/divisor)
        return min(result, 2**31 -1)
        """
        iterations = 0
        if (divisor < 0 and dividend < 0) or (divisor > 0 and dividend > 0):
            negative = False
        else:
            negative = True
        
        divisor = abs(divisor)
        dividend = abs(dividend)
        while dividend >= divisor:
            dividend -= divisor
            iterations+=1
            
        if negative:
            return -min(iterations, 2**31-1)
        else:
            return min(iterations, 2**31-1)
        """