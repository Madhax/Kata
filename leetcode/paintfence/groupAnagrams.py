class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)
        for word in strs:
            hist = Counter(word)
            sig = tuple([(key, hist[key]) for key in sorted(hist.keys())])
            d[sig].append(word)
            
            
        #print(d)
        return [list(d[key]) for key in d.keys()]