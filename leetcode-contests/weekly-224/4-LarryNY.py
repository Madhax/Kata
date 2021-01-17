class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        
        fx = fy = None
        mx = my = None
        cx = cy = None
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        @lru_cache(None)
        def catWin(mx, my, cx, cy, turn):
            if cx == fx and cy == fy:
                return True
            if mx == cx and my == cy:
                return True
            
            for dx, dy in directions:
                for s in [-1, 1]:
                    for k in range(1, catJump + 1):
                        nx, ny = cx + s * k * dx, cy + s * k * dy

                        if nx == fx and ny == fy:
                            return True
                        
                        if mx == nx and my == ny:
                            return True

                        if not (0 <= nx < rows and 0 <= ny < cols):
                            break
                            
                        if grid[nx][ny] == '#':
                            break

                        if not mouseWin(mx, my, nx, ny, turn + 1):
                            return True

            if not mouseWin(mx, my, cx, cy, turn + 1):
                return True
                        
            return False
        
        @lru_cache(None)
        def mouseWin(mx, my, cx, cy, turn):
            if mx == fx and my == fy:
                return True
            if turn >= 80:
                return False
            
            for dx, dy in directions:
                for s in [-1, 1]:
                    for k in range(1, mouseJump + 1):
                        nx, ny = mx + s * k * dx, my + s * k * dy

                        if nx == fx and ny == fy:
                            return True
                        
                        if not (0 <= nx < rows and 0 <= ny < cols):
                            break

                        if grid[nx][ny] == '#':
                            break
                            
                        if not catWin(nx, ny, cx, cy, turn + 1):
                            return True

            return False
            
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 'F':
                    fx, fy = x, y
                elif grid[x][y] == 'C':
                    cx, cy = x, y
                elif grid[x][y] == 'M':
                    mx, my = x, y
        
        return mouseWin(mx, my, cx, cy, 0)
