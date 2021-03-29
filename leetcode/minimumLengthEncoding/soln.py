class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        cands = set()
        #words.sort(key=lambda x: len(x), reverse=True)
        #print(words)
        def isSubset(word, subword):
            for x in range(1, len(subword)+1):
                if word[-x] != subword[-x]:
                    return False
            return True
        canditer = 0
        skip = set()
        
        for word in words:
            cands.add(word)
            
        for word in words:
            for x in range(1, len(word)):
                cand = word[x:]
                if cand in cands:
                    cands.remove(cand)
        """
        while canditer < len(words):
            worditer = canditer + 1
            if canditer not in skip:
                while worditer < len(words):
                    if len(words[worditer]) == len(words[canditer]):
                        worditer += 1
                        continue
                    if worditer not in skip and words[worditer] == words[canditer][len(words[canditer]) - len(words[worditer]):]:
                    #if worditer not in skip and isSubset(words[canditer], words[worditer]):
                        skip.add(worditer)
                        #words.pop(worditer)
                    else:
                        worditer += 1
                cands.add(words[canditer])
                    
            canditer += 1
        """
        
        #print(cands)
        return sum(len(x) for x in cands) + len(cands)