class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        @functools.cache
        def generate(n: int) -> List[str]:
            if n == 0: return ['']
            if n == 1: return ['()']
            
            result = []
            for x in range(n):
                for l in generate(x):
                    for r in generate(n-1-x):
                        result.append("(" + l + ")" + r)
            
            return result
        
        return generate(n)
        