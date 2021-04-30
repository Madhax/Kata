class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        
        #states
        #index, hasLowerCase, hasUpperCase, hasDigit, conSecutive
        
        @functools.cache
        def dp(index, length, hasLowerCase, hasUpperCase, hasDigit, consecutives):
            if index == len(password):
                if length > 20:
                    retVal = length - 20
                    retVal += 1 if not hasLowerCase else 0
                    retVal += 1 if not hasUpperCase else 0
                    retVal += 1 if not hasDigit else 0
                    return retVal
                
                retVal = 0
                retVal += 1 if not hasLowerCase else 0
                retVal += 1 if not hasUpperCase else 0
                retVal += 1 if not hasDigit else 0
                
                
                if length + retVal < 6:
                    #print(index, retVal)
                    retVal += 6 - (length+retVal)
                    return retVal
                
                return retVal
                        
                
                
                """
                return () + \
                    () + \
                    () + \
                    (6 - index if index < 6 else 0) + \
                    index - 20 if index > 20 else 0 
            
                """
            if length >= 20:
                return dp(index+1, length+1, hasLowerCase, hasUpperCase, hasDigit, consecutives)
            
            best = math.inf
            
            newHasDigit, newHasUpperCase, newHasLowerCase = hasDigit, hasUpperCase, hasLowerCase
            
            #new vals
            if '0' <= password[index] <= '9':
                newHasDigit = True
            elif 'A' <= password[index] <= 'Z':
                newHasUpperCase = True
            elif 'a' <= password[index] <= 'z':
                newHasLowerCase = True
            
            if index > 0:
                if password[index] == password[index-1]:
                    if consecutives == 2:
                        #we must replace
                        best = min(best, 1 + dp(index+1, length+1, True, hasUpperCase, hasDigit, 0))
                        best = min(best, 1 + dp(index+1, length+1, hasLowerCase, True, hasDigit, 0))
                        best = min(best, 1 + dp(index+1, length+1, hasLowerCase, hasUpperCase, True, 0))
                        
                        #add
                        best = min(best, 1 + dp(index, length+1, True, hasUpperCase, hasDigit, 0))
                        best = min(best, 1 + dp(index, length+1, hasLowerCase, True, hasDigit, 0))
                        best = min(best, 1 + dp(index, length+1, hasLowerCase, hasUpperCase, True, 0))
                        
                    else:
                        best = min(best, dp(index+1, length+1, newHasLowerCase, newHasUpperCase, newHasDigit, consecutives+1))
                
                else:
                    best = min(best, dp(index+1, length+1, newHasLowerCase, newHasUpperCase, newHasDigit, 1))
            else:      
                best = min(best, dp(index+1, length+1, newHasLowerCase, newHasUpperCase, newHasDigit, 1))
            
            return best
                    
        best = dp(0, 0, False, False, False, 0)
        iter = 1
        while len(password) - iter >= 20:
            best = min(best, iter + dp(iter, 0, False, False, False, 0))
            iter += 1
            
        return best