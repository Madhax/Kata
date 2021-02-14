class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        R = len(grid) -1
        C = len(grid[0]) - 1
        
        if grid[0][0] == 1:
            return -1
        
        def bfs():
            nonlocal grid
            
            q = deque()
            seen = set()
            
            q.append([0,0,1])
            seen.add((0,0))
            while len(q) > 0:
                
                x, y, iteration = q.popleft()
                
                #print(x, y, iteration)
                if x == R and y == C:
                    return iteration
                
                #directions
                newx, newy = max(0, x-1), max(0, y-1)
                if (newx, newy) not in seen and grid[newy][newx] == 0:
                    seen.add((newx, newy))
                    q.append([newx, newy, iteration+1])
                    
                newx, newy = max(0, x-1), max(0, y)
                if (newx, newy) not in seen and grid[newy][newx] == 0:
                    seen.add((newx, newy))
                    q.append([newx, newy, iteration+1])
                    
                newx, newy = max(0, x), max(0, y-1)
                if (newx, newy) not in seen and grid[newy][newx] == 0:
                    seen.add((newx, newy))
                    q.append([newx, newy, iteration+1])
                    
                newx, newy = max(0, x-1), min(R, y+1)
                if (newx, newy) not in seen and grid[newy][newx] == 0:
                    seen.add((newx, newy))
                    q.append([newx, newy, iteration+1])
                    
                newx, newy = max(0, x), min(R, y+1)
                if (newx, newy) not in seen and grid[newy][newx] == 0:
                    seen.add((newx, newy))
                    q.append([newx, newy, iteration+1])
                
                
                newx, newy = min(C, x+1), max(0, y-1)
                if (newx, newy) not in seen and grid[newy][newx] == 0:
                    seen.add((newx, newy))
                    q.append([newx, newy, iteration+1])
                    
                newx, newy = min(C, x+1), max(0, y)
                if (newx, newy) not in seen and grid[newy][newx] == 0:
                    seen.add((newx, newy))
                    q.append([newx, newy, iteration+1])
                    
                newx, newy = min(C, x+1), min(R, y+1)
                if (newx, newy) not in seen and grid[newy][newx] == 0:
                    seen.add((newx, newy))
                    q.append([newx, newy, iteration+1])
            
            return -1
                
        return bfs()
            
            