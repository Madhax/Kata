class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        ctr = Counter(arr)
        N = len(arr)
        repeats = [ctr[key] for key in ctr.keys()]
        repeats.sort()
        
        setSize = 0
        numRemoved = 0
        while numRemoved < (N/2):
            setSize += 1
            numRemoved += repeats.pop()
            
        return setSize
        