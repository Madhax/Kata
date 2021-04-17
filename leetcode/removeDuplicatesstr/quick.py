class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        remove = []
        ## Generating possible duplicates
        for ch in set(s):
            remove.append(ch*k)
            
        old,new = s,s
        while True:
            for candidate in remove:
                new = new.replace(candidate,"")
            if len(old) == len(new):
                break
            old = new        
        return old
        