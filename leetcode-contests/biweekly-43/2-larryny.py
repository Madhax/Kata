class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        score = 0
        
        stack = []
        if x > y:
            for c in s:
                stack.append(c)
                
                while len(stack) >= 2:
                    if stack[-2] == "a" and stack[-1] == "b":
                        stack.pop()
                        stack.pop()
                        
                        score += x
                    else:
                        break
        else:
            for c in s:
                stack.append(c)
                
                while len(stack) >= 2:
                    if stack[-2] == "b" and stack[-1] == "a":
                        stack.pop()
                        stack.pop()
                        
                        score += y
                    else:
                        break
        
        #print(f"{score=} {stack=}")
        stack2 = []
        for c in stack:
            stack2.append(c)
            
            while len(stack2) >= 2:
                if stack2[-2] == "a" and stack2[-1] == "b":
                    stack2.pop()
                    stack2.pop()

                    score += x
                elif stack2[-2] == "b" and stack2[-1] == "a":
                    stack2.pop()
                    stack2.pop()

                    score += y
                else:
                    break
        
        return score
