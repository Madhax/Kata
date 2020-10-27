class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # shrink cache of size query_row ^ 2  to query_row.
        glasses = [poured] + [0] * query_row
        print(glasses)
        # In-place expansion to save memory
        for r in range(query_row):
            #reverse traversal sequence
            for c in range(r, -1, -1):
                overflow = 0
                
                # if the glass above overflows
                if glasses[c] > 1:
                    overflow = (glasses[c] - 1) / 2
                    glasses[c+1] += overflow
                    
                glasses[c] = overflow
                
                
        return min(1, glasses[query_glass])