class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        for i, c in Counter(words).items():
            indexj = 0
            for j in i:
                indexj = s.find(j, indexj) + 1
                if not indexj:
                    break
            else:
                count +=c
        return count