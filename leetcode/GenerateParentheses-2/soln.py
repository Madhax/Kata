class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def recurse(n):
            if n == 1:
                return ["()"]
            
            cands = recurse(n-1)
            res = set()
            for cand in cands:
                res.add("(" + cand + ")")
                res.add("()" + cand)
                res.add(cand + "()")
                #replace every () w/ (())
                idx  = cand.find("(", 0)
                while idx >= 0:
                    res.add(cand[:idx+1] + "()" + cand[idx+1:])
                    idx  = cand.find("(", idx+1)
                
            return res
        
        return recurse(n)