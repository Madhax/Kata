class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = {}
        rows[1] = [1]
               
        for row in range(2, numRows+1):
            prevRow = rows[row-1]
            nextRow = []
            
            nextRow.append(1) # Start padding
            
            # Mid calculation
            for i in range(len(prevRow) - 1): 
                nextRow.append(prevRow[i] + prevRow[i+1])
            
            nextRow.append(1) # End padding
            
            rows[row] = nextRow

        ans = []
        
        for row in rows.values():
            ans.append(row)
        
        return ans