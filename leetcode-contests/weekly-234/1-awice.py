class Solution(object):
    def numDifferentIntegers(self, word):
        seen = set()
        for k,grp in groupby(word, key=lambda c: c.isdigit()):
            if k:
                s = "".join(grp)
                seen.add(int(s))
        return len(seen)