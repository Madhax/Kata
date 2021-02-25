class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        scoreStack = []
        finalScore = 0
        scoreStack.append(0)
        for x in S:
            if x == "(":
                scoreStack.append(0)
               
            elif x == ")":
                score = scoreStack.pop()
                if score == 0:
                    scoreStack[-1] += 1
                else:
                    scoreStack[-1] += (2*score)
            #print(x, scoreStack)
        #print(scoreStack)
        return scoreStack[-1]