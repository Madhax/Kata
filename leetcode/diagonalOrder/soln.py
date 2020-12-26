class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        y, x = 0, 0
        if len(matrix) == 0:
            return []
        edgey, edgex = len(matrix)-1, len(matrix[0])-1
        directionUp = True
        output = []
        while y <= edgey and x <= edgex:
            output.append(matrix[y][x])
            
            if y == edgey and x == edgex:
                break
                
            if directionUp:
                if y == 0:
                    directionUp = False
                    
                    if x == edgex:
                        y += 1
                        
                    else:
                        x += 1
                    
                elif x == edgex:
                    y += 1
                    directionUp = False
                    
                else:
                    x += 1
                    y -= 1
                    
            else:
                if x == 0:
                    directionUp = True
                    
                    if y == edgey:
                        x += 1
                        
                    else:
                        y += 1
                    
                elif y == edgey:
                    x += 1
                    directionUp = True
                    
                else:
                    x -= 1
                    y += 1
                    
                
            
        return output