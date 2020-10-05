import math

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0: 
            return 1
        if N == 1:
            return 0
        bitfloat = math.log(N,2)
        bits = math.ceil(bitfloat)
        if float(bits) == bitfloat:
            bits += 1
        #print(bits)
        return N ^ int('1'*bits, 2)