class Solution:
    def minimumDeletions(self, s: str) -> int:
        total = collections.Counter(s)

        best = len(s)
        a = total["a"]
        b = 0
        for x in s:
            if x == "a":
                best = min(best, b + a)
                a -= 1
            else:
                best = min(best, b + a)
                b += 1
                
        best = min(best, b + a)
        
        return best