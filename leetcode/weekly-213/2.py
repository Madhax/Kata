class Solution:
    ctr = 0
    def countVowelStrings(self, n: int) -> int:
        self.ctr = 0
       
        #5,
        #5 + 4 + 3 + 2 + 1
        #15*5 +  15*4 + 15*3 +  15*2 +  15*1
       
        def recursive(offset, depth, maxdepth):
            if depth == maxdepth:
                self.ctr += 1
                return
           
            for x in range(offset, 5):
                recursive(x, depth+1, maxdepth)
               
       
        recursive(0, 0, n)
        return self.ctr