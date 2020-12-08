class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for x in range(n)]

        iter = 1
        x, y = 0, 0
        state = 0
        lowerX, lowerY, upperX, upperY = 0, 0, n-1, n-1
       
        while iter != n*n + 1:
            matrix[y][x] = iter
           
            if state == 0:
                x += 1
                if x == upperX:
                    lowerY += 1
                    state = 1
                   
            elif state == 1:
                y += 1
                if y == upperY:
                    upperX -= 1
                    state = 2
               
            elif state == 2:
                x -= 1
                if x == lowerX:
                    upperY -= 1
                    state = 3
               
            elif state == 3:
                y -= 1
                if y == lowerY:
                    lowerX += 1
                    state = 0
               
            else:
                return 0
               
            iter += 1
           
        return matrix
