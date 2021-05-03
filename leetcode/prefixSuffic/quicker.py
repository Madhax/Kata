class WordFilter:

    def __init__(self, words: List[str]):
        self.pref = collections.defaultdict(set)
        self.suff = collections.defaultdict(set)
        seen = set()
        for i in range(len(words)-1, -1, -1):
            w = words[i]
            if w in seen:
                continue
            seen.add(w)
            for j in range(len(w)+1):
                self.pref[w[:j]].add(i)
                self.suff[w[j:]].add(i)

    def f(self, prefix: str, suffix: str) -> int:
        a = self.pref[prefix]
        b = self.suff[suffix]
        x = a & b
        return max(x) if x else -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)