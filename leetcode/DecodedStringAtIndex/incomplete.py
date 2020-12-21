class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        stringIndex = 0
        
        stringStack = []
        intStack = []
        offset = 0
        
        def getIntegerAtIndex(S, index):
            retNum = ""
            while index < len(S) and S[index].isdigit():
                retNum += S[index]
                index += 1
            
            return (int(retNum), index)
        
        def recurse():
            nonlocal stringStack, intStack, K, S
            
            strLen = 0
            
            for string, multiplier in zip(stringStack, intStack):
                strLen += len(string)
                strLen *= (multiplier-1)
                
            if strLen >= K:
                #print("Able to find in", stringStack, intStack)
                #unwrap
                strLen = 0
                slidingWindow = ""
                baseString = ""
                for string, multiplier in zip(stringStack, intStack):
                    slidingWindow += string
                    strLen += len(string)
                    adder = slidingWindow
                    multiplier -= 1
                    while multiplier > 0:
                        #print(slidingWindow, string, multiplier)
                        strLen += len(adder)
                        slidingWindow += adder

                        if strLen >= K:
                            #print(slidingWindow, strLen)
                            return (True, slidingWindow[-1 - (strLen-K)])
                        
                        multiplier -= 1
                        
                    #baseString = slidingWindow
                        
            return (False,'')
        
        currentString = ""
        
        while stringIndex < len(S):   
            if S[stringIndex].isalpha():
                currentString += S[stringIndex]
                stringIndex += 1
                
                offset += 1
                if offset == K:
                    return currentString[-1]
                
            elif S[stringIndex].isdigit():
                numberOfTimes = getIntegerAtIndex(S, stringIndex)
                stringStack.append(currentString)
                intStack.append(numberOfTimes[0])
                stringIndex = numberOfTimes[1]
                
                (found, letter) = recurse()
                if found:
                    return letter
                currentString = ""
                #
                
        return 'P'
                