from collections import defaultdict
class Solution:
    def solve(self, relations):
        
        follows = defaultdict(set)
        for follow in relations:
            follows[follow[0]].add(follow[1])

        output = []

        for x in follows.keys():
            for b in follows[x]:
                if b in follows and x in follows[b]:
                    output.append(x)
                    break

        output.sort()
        return output
        
        #return [x in follows.keys() where ]