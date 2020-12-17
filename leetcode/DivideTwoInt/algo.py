class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign_out = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)

        place_values = []
        current = divisor
        while current <= dividend:
            place_values.append(current)
            current = current << 1
        print(place_values)
        quotient = 0
        for v in reversed(place_values):
            quotient = quotient << 1
            if v <= dividend:
                quotient += 1
                dividend -= v
        
        res = sign_out * quotient

        if not (-(1 << 31) <= res <= (1 << 31) - 1):
            return (1 << 31) - 1
        return res