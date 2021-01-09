class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        newcode = [0] * len(code)
        
        if k > 0:
            for x in range (0, len(code)):
                newk = k
                while newk > 0:
                    newcode[x] += code[(newk + x) % len(code)]
                    newk -= 1
            
        elif k < 0:
            for x in range (0, len(code)):
                newk = k
                while newk < 0:
                    newcode[x] += code[(x) + (abs(newk) % len(code)) * -1]
                    newk += 1
        
        code = newcode
        return code