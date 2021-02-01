class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n=len(encoded)+1
        L=[0]
        for x in encoded:
            L.append(L[-1]^x)
        z=0
        for x in L:
            z=z^x
        for x in range(1,n+1):
            z=z^x
        return [z^x for x in L]