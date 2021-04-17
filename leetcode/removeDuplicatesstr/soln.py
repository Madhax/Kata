class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        while True:
            found = False
            parts = [list(g) for k, g in groupby(s)]
            for part in parts:
                if len(part) >= k:
                    part[:] = part[k:]
                    found = True
            #print(parts)
            s = "".join(["".join(group) for group in parts])
            if found is False:
                break
        return s