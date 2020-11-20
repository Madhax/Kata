class Solution:
    def decodeString(self, s: str) -> str:
        output = []
        def repeat(substring, iterations):
            nonlocal output
           
            for iter in range(iterations):
                x = 0
                while x < len(substring):
                    element = substring[x]
                    numIterations = 0
                    if element.isdigit():
                        iterationDigits = [element]
                        y = x + 1
                        while substring[y].isdigit():
                            iterationDigits.append(substring[y])
                            y+=1
                        x = y - 1
                        numIterations=int("".join(iterationDigits))
                        #fix here
                        z = x+2
                        numBrackets = 1
                        while numBrackets > 0:
                            if substring[z] == "]":
                                numBrackets -= 1
                            elif substring[z] == "[":
                                numBrackets += 1
                            z += 1
                       
                        lastIndex = z-1
                        newSubstring = substring[x+2:lastIndex]
                        repeat(newSubstring, numIterations)
                        x = lastIndex
                    else:
                        output.append(element)
                   
                    x += 1
                   
                   
                   
           
        repeat(s, 1)
        return "".join(output)
