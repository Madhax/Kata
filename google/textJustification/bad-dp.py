class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        state = defaultdict(lambda: (math.inf, 0))
        
        @functools.cache
        def dp(line, index):
            if index == len(words):
                return 0
            
            best = math.inf
            
            cost = maxWidth
            for x in range(index, len(words)):
                cost -= len(words[x])
                if cost < (x-index):
                    break

                cand = cost + dp(line + 1 , x+1)
                if line == 1:
                    print(x, cand, cost, dp(line+1, x+1), index)
                if cand <= best:
                    best = cand
                    bestIndex = x+1

            if line == 1:
                
                print("here", best,bestIndex)
                print(state)
            state[line] = min((best, bestIndex), state[line])
            return best
        
        dp(0,0)
        print(state)
        output = []
        index = 0
        line = 0
        output = []
        while index < len(words):
            _, wordLim = state[line]
            
            wordCand = []
            for x in range(index, wordLim):
                wordCand.append(words[x])
            
            if len(wordCand) == 1:
                wordCand.append("")
                
            spaces = maxWidth - sum([len(x) for x in wordCand])
            if wordLim < len(words):
                spaceIndex = 1
                while spaces > 0:
                    wordCand[spaceIndex] = " " + wordCand[spaceIndex]
                    spaceIndex += 1
                    spaces -= 1
                    if spaceIndex == len(wordCand):
                        spaceIndex = 1
            elif spaces > 0:
                for x in range(1, len(wordCand)):
                    wordCand[x] = " " + wordCand[x]
                    spaces -= 1
                    if spaces == 0:
                        break
                        
                wordCand[-1] += " " * spaces
            #print(wordCand)
            output.append("".join(wordCand))
            index = wordLim
            line += 1
        
        return output
        #print (dp(0, 0))
        
        #print(state)
        return ""
        
        