class Solution:
    def solve(self, s, t):

        diffIndices = []
        sset = set()
        tset = set()
        letterst = {}
        letterss = {}
        for x in range(len(s)):
            if s[x] != t[x]:
                diffIndices.append(x)
                sset.add(x)
                tset.add(t)

                if t[x] not in letterst:
                    letterst[t[x]] = [x]
                else:
                    letterst[t[x]].append(x)

                if s[x] not in letterss:
                    letterss[s[x]] = [x]
                else:
                    letterss[s[x]].append(x)

        numFound = 0

        for key in letterss.keys():
            if key in letterst:
                for y in letterst[key]:
                    for x in letterss[key]:
                        if y != x:
                            numFound = 1
                            print(x,y, s[y], )
                            if x in tset and y in sset and s[y] == t[x]:
                                return len(diffIndices) - 2





        return len(diffIndices) - numFound

        
