class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        numDigits = len(str(n))
        maxDigits = [int(char) for char in str(n)]
        digits = set([int(char) for char in digits])
        digits.add(0)
       
        #print(numDigits)
        #print(maxDigits)
        #print(digits)
        @lru_cache(maxsize=None)
        def countCombinations(offset, leadingZero, maxDigit):
            #print(offset, leadingZero, maxDigit)
            nonlocal digits, numDigits
            if offset == 0:
                return 1
            ctr = 0
            #print(digits)
            for digit in digits:
                #print(digit, offset)
                if digit == 0:
                    if leadingZero and offset != 1:
                        #rint("here")
                        ctr += countCombinations(offset-1, leadingZero, False)
                    #lif offset == numDigits:
                    #   ctr += countCombinations(offset-1, True, False)
                   
                elif maxDigit:
                   
                    if digit < maxDigits[numDigits-offset]:
                        #print(digit, maxDigits[numDigits-offset])
                        ctr += countCombinations(offset-1, False, False)
                       
                    elif digit == maxDigits[numDigits-offset]:
                        #print(digit, maxDigits[numDigits-offset])
                        ctr += countCombinations(offset-1, False, True)
                       
                else:
                    #if leadingZero == True:
                    #    print("here", offset)
                    ctr += countCombinations(offset-1, False, False)
                     
            #print(offset, ctr)        
            return ctr
       
        return countCombinations(numDigits, True, True)

   