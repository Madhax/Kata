class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        #sliding window targetting T or F
        
        cand1 = 0
        cand2 = 0
        
        #assume true
        work = []
        curk = k
        
        for c in answerKey:
            if c == "T":
                work.append(c)
            elif c == "F":
                if curk:
                    work.append(c)
                    curk -= 1
                    
                else:
                    while curk == 0:
                        val = work.pop(0)
                        if val == "F":
                            curk += 1
                            
                    work.append(c)
                    curk -= 1
                    
            cand1 = max(cand1, len(work))
                
            
        #assume false
        work = []
        curk = k
        
        for c in answerKey:
            if c == "F":
                work.append(c)
            elif c == "T":
                if curk:
                    work.append(c)
                    curk -= 1
                    
                else:
                    while curk == 0:
                        val = work.pop(0)
                        if val == "T":
                            curk += 1
                            
                    work.append(c)
                    curk -= 1
                    
            cand2 = max(cand2, len(work))
        
        
        return max(cand1, cand2)
