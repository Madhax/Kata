class Solution:
    memoize = dict()
    def recursiveSoln(self, s: str, wordDict: List[str], offset: int) -> bool:
       
        if(offset in self.memoize):
            return self.memoize[offset]
       
        for word in wordDict:
            if(s.startswith(word, offset)):
                if(len(word)+offset == len(s)):
                    return True
                else:
                    if(self.recursiveSoln(s, wordDict, offset+len(word))):
                        return True
       
        self.memoize[offset] = False
        return False
   
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memoize.clear()
               
        if(self.recursiveSoln(s, wordDict, 0)):
            return True
       
        return False
