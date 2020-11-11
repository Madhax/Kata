class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        B = [[] * len(A)]
        for row in A:
            for j in range((len(row) + 1) // 2):
                row[j], row[~j] = row[~j] ^ 1, row[j] ^ 1
        
        return A 