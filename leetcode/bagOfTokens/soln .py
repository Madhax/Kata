import functools
class Solution:
    maxScore = 0
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
       
        i = 0
        j = len(tokens)-1
        score = 0
        maxScore = 0
        while True:
            #print(i, j, score)
            maxScore = max(score, maxScore)
            if i > j:
                break
           
            if P >= tokens[i]:
                score += 1
                P -= tokens[i]
                i += 1
                continue
               
            elif score > 0:
                score -= 1
                P += tokens[j]
                j -= 1
                continue
            else:
                break
        return maxScore