class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        state = {}
        
        @functools.cache
        def greedy(line, index):
            width = maxWidth
            #print(line, index)
            if index == len(words):
                state[line] = index
                return
            
            for x in range(index, len(words)):
                width -= len(words[x])
                if width < x-index:
                    x -= 1
                    break
                    
                greedy(line+1, x+1)
                
        
            state[line] = x + 1
            
        greedy(0, 0)
        #print(state)
        output = []
        index = 0
        line = 0
        output = []
        while index < len(words):
            wordLim = state[line]
            
            wordCand = []
            for x in range(index, wordLim):
                wordCand.append(words[x])
            
            if len(wordCand) == 1:
                wordCand.append("")
                
            #print(wordCand)
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
        
        