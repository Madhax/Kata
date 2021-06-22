class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        response = []
        
        for x in range(numRows):
            #print(response, x)
            if x == 0:
                response.append([1])
                continue
            work = []
            for c in range(x+1):
                
                if c == 0 or c == x:
                    work.append(1)
                else:
                    #print(x-1,c,response)
                    work.append(response[x-1][c] + response[x-1][c-1])
            
            response.append(work)
        return response