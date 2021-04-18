class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        cs = Counter()
        for c in sentence:
            cs[c] += 1
            
        return len(cs.values()) == 26