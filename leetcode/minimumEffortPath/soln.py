from collections import deque
from collections import defaultdict

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        def bfs():
            nonlocal heights
            goaly = len(heights) - 1
            goalx = len(heights[0]) - 1
            
            q = deque()
            
            seen = defaultdict(lambda: defaultdict(lambda: math.inf))
            
            #y, x, work
            q.append((0, 0, 0))
            
            best = math.inf
            
            while len(q):
                
                (y, x, currentwork) = q.popleft()
                
                if y == goaly and x == goalx:
                    if currentwork < best:
                        best = currentwork
                    continue
                    
                if seen[y][x] < currentwork:
                    continue
                    
                currentheight = heights[y][x]
                #up
                
                if y > 0:
                    targety = y-1
                    targetx = x
                    targetwork = max(currentwork, abs(currentheight - heights[targety][targetx]))
                    
                    if targetwork < seen[targety][targetx]:
                        seen[targety][targetx] = targetwork
                        q.append((targety, targetx, targetwork))
                        
                #down
                if y < len(heights)-1:
                    targety = y+1
                    targetx = x
                    targetwork = max(currentwork, abs(currentheight - heights[targety][targetx]))
                    
                    if targetwork < seen[targety][targetx]:
                        seen[targety][targetx] = targetwork
                        q.append((targety, targetx, targetwork))
                        
                #left
                if x > 0:
                    targety = y
                    targetx = x-1
                    targetwork = max(currentwork, abs(currentheight - heights[targety][targetx]))
                    
                    if targetwork < seen[targety][targetx]:
                        seen[targety][targetx] = targetwork
                        q.append((targety, targetx, targetwork))
                        
                #right
                if x < len(heights[0]) -1:
                    targety = y
                    targetx = x+1
                    targetwork = max(currentwork, abs(currentheight - heights[targety][targetx]))
                    
                    if targetwork < seen[targety][targetx]:
                        seen[targety][targetx] = targetwork
                        q.append((targety, targetx, targetwork))
                        
                    
                
            return best
        
        return bfs()
