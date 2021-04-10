class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for index, c in enumerate(order):
            d[c] = index
       
        words2 = words.copy()
        words2.sort(key=lambda x: tuple([d[i] for i in x]))
       
        return words == words2

