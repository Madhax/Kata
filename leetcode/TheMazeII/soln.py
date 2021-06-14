class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        
        seen = set()
        #seen.add((start[0], start[1]))
        q = [(0, start[0], start[1])]
        
        
        while len(q) > 0:
            dist, y, x = heappop(q)
            if (y,x) in seen:
                continue
                
            seen.add((y, x))
        
            if y == destination[0] and x == destination[1]:
                return dist
            
            #findup
            ndist = dist
            ny = y
            while 0 <= ny - 1 and maze[ny-1][x] != 1:
                ndist += 1
                ny -= 1
                
            if (ny, x) not in seen:
                #seen.add((ny,x))
                heappush(q, (ndist, ny, x))
                
            #down  
            ndist = dist
            ny = y
            while ny + 1 < len(maze) and maze[ny+1][x] != 1:
                ndist += 1
                ny += 1
                
            if (ny, x) not in seen:
                #seen.add((ny,x))
                heappush(q, (ndist, ny, x))
                
            #left
            ndist = dist
            nx = x
            while 0 <= nx - 1 and maze[y][nx-1] != 1:
                ndist += 1
                nx -= 1
                
            if (y, nx) not in seen:
                #seen.add((y,nx))
                heappush(q, (ndist, y, nx))
            
            #right
            ndist = dist
            nx = x
            while nx + 1 < len(maze[0]) and maze[y][nx+1] != 1:
                ndist += 1
                nx += 1
                
            if (y, nx) not in seen:
                #seen.add((y,nx))
                heappush(q, (ndist, y, nx))
            
                
        return -1