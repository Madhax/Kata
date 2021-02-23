class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (len(x), x), reverse=True)
       
        def isSubsequence(word):
           
            siter = witer = 0
           
            while siter < len(s):
                if s[siter] == word[witer]:
                    witer += 1
                    if witer == len(word):
                        return True
               
                siter += 1
           
            return False
           
        best = ""
        for val in d:
            if isSubsequence(val):
                if best == "":
                    best = val
                elif len(val) == len(best):
                    best = val
                else:
                    break
        #print(d)
        return best
