class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            row.reverse()
            for index in range(0, len(row)):
                row[index] = (row[index] + 1) % 2
           
        return A 