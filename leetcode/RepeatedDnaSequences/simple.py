class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
        
        seen = set()
        res = set()
        for i in range(len(s)):
            new = s[i: i+10]
            if new in seen:
                res.add(new)
            else:
                seen.add(new)
        return res