class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        allCombs = set()
        iter = 0
        while iter <= len(s) - k:
            allCombs.add(s[iter:iter+k])
            iter += 1
           
        #print(len(allCombs))
        return len(allCombs) == 2**k