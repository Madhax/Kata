class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        s1 = set(word1)
        s2 = set(word2)
        if (s1 != s2):
            return False
        a1 = []
        a2 = []
        for c in s1:
            a1.append(word1.count(c))
        for c in s2:
            a2.append(word2.count(c))
        return sorted(a1) == sorted(a2)