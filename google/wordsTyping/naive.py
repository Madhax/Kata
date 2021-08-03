class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        
        numFitted = 0
        sentenceIter = 0
        curRow = 0
        curCol = 0
        wordIter = 0
        
        totalSentence = len("".join(sentence)) + len(sentence) 
        sentencesPerRow = (cols // totalSentence) - 1
        greedyFitted = (totalSentence * sentencesPerRow) - 1
        
        canGreedy = False
        if sentencesPerRow > 0:
            canGreedy = True
        
        while True:
            curLen = len(sentence[wordIter])
            
            if canGreedy and greedyFitted <= cols - curCol:
                curCol += greedyFitted + 1
                numFitted += sentencesPerRow
                
            elif curLen <= cols - curCol:
                wordIter += 1
                if wordIter == len(sentence):
                    wordIter = 0
                    numFitted += 1
                
                curCol += curLen + 1
            else:
                curCol = 0
                curRow += 1
                if curRow == rows:
                    break
            
        return numFitted