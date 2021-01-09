class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return [i for j in word1 for i in j] == [i for j in word2 for i in j] 