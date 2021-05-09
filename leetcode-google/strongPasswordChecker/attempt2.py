class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        
        #states
        #index, hasLowerCase, hasUpperCase, hasDigit, conSecutive
        
        @functools.cache
        def dp(index, length, hasLowerCase, hasUpperCase, hasDigit, consecutives, prevChar):
            if length > 20:
                return math.inf

            if index == len(password):
                if length < 6:
                    return math.inf
                    
                return hasLowerCase == True and hasUpperCase == True and hasDigit == True

            if consecutives >= 3:
                return math.inf
            
            best = math.inf
            
            newHasDigit, newHasUpperCase, newHasLowerCase = hasDigit, hasUpperCase, hasLowerCase
            
            #new vals
            if '0' <= password[index] <= '9':
                newHasDigit = True
            elif 'A' <= password[index] <= 'Z':
                newHasUpperCase = True
            elif 'a' <= password[index] <= 'z':
                newHasLowerCase = True
           
            if password[index] == prevChar:
                best = min(best, dp(index+1, length+1, newHasLowerCase, newHasUpperCase, newHasDigit, consecutives+1, password[index]))
        
            #skip
            best = min(best, dp(index+1, length+1, newHasLowerCase, newHasUpperCase, newHasDigit, consecutives, password[index]))

            #replace
            best = min(best, 1 + dp(index+1, length+1, True, hasUpperCase, hasDigit, 0, ''))
            best = min(best, 1 + dp(index+1, length+1, hasLowerCase, True, hasDigit, 0, ''))
            best = min(best, 1 + dp(index+1, length+1, hasLowerCase, hasUpperCase, True, 0, ''))
            
            #add
            best = min(best, 1 + dp(index, length+1, True, hasUpperCase, hasDigit, 0, ''))
            best = min(best, 1 + dp(index, length+1, hasLowerCase, True, hasDigit, 0, ''))
            best = min(best, 1 + dp(index, length+1, hasLowerCase, hasUpperCase, True, 0, ''))

            #delete
            best = min(best, 1 + dp(index+1, length, hasLowerCase, hasUpperCase, hasDigit, consecutives, prevChar))
            best = min(best, 1 + dp(index+1, length, hasLowerCase, hasUpperCase, hasDigit, consecutives, prevChar))
            best = min(best, 1 + dp(index+1, length, hasLowerCase, hasUpperCase, hasDigit, consecutives, prevChar))
            
            return best
                    
        best = dp(0, 0, False, False, False, 0, '')
        """
        iter = 1
        while len(password) - iter >= 20:
            best = min(best, iter + dp(iter, 0, False, False, False, 0))
            iter += 1
        """            
        return best