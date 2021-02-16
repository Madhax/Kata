class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        strength = [(i, j) for i, j in enumerate([sum(x) for x in mat])]
        strength.sort(key=lambda x: x[1])
        return [x[0] for x in strength[:k]]