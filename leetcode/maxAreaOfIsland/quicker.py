class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        
        if num_rows < 1:
            return 0
        
        num_columns = len(grid[0])
        
        grid_copy = grid.copy()
        
        max_area = 0
        for row in range(num_rows):
            for column in range(num_columns):
                if grid_copy[row][column] == 1:
                    grid_copy[row][column] = 0
                    stack = [(row, column)]
                    area = 0
                    while stack:
                        r, c = stack.pop()
                        area += 1
                        if r > 0 and grid_copy[r-1][c] == 1:
                            stack.append((r-1, c))
                            grid_copy[r-1][c] = 0
                        if r < num_rows - 1 and grid_copy[r+1][c] == 1:
                            stack.append((r+1, c))
                            grid_copy[r+1][c] = 0
                        if c > 0 and grid_copy[r][c-1] == 1:
                            stack.append((r, c-1))
                            grid_copy[r][c-1] = 0
                        if c < num_columns - 1 and grid_copy[r][c+1] == 1:
                            stack.append((r, c+1))
                            grid_copy[r][c+1] = 0
                    max_area = max(max_area, area)
        
        return max_area