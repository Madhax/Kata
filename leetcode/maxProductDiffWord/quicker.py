class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = {sum(1 << (ord(c) - 97) for c in set(w)): len(w) for w in sorted(words, key=len)}
        return max([d[k] * d[K] for k, K in itertools.combinations(d.keys(), 2) if not K & k] or [0])