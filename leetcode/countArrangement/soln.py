class Solution:
    def countArrangement(self, n: int) -> int:
        self.output = 0
        def dfs(posn, cands):
            nonlocal n
            
            if posn == n and (cands[0] % posn == 0 or posn % cands[0] == 0):
                #print(posn, cands[0])
                self.output += 1
                return 
            
            elif posn==n:
                ##print(cands[0])
                return
            
            for index, val in enumerate(cands):
                if val % posn == 0 or posn % val == 0:
                    dfs(posn+1, cands[index+1:] + cands[:index])
        
        #print(list(range(1, n+1)))
        dfs(1, list(range(1, n+1)))
        return self.output