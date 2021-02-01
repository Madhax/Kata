from collections import defaultdict
class Solution:
    def solve(self, s):
        depth = 0
        xs = defaultdict(int)

        for symbol in s:
            if symbol == "(":
                depth += 1
            elif symbol == ")":
                xs[depth] = xs[depth]
                depth -= 1
            
            elif symbol == "X":
                xs[depth] += 1
        
        output = []
        for x in sorted(xs.keys()):
            output.append(xs[x])
        return output