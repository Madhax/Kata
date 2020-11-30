from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        q = deque()
        visited = {}
        
        q.append(start)
        
        while len(q):
            currentNode = q.popleft()
            if arr[currentNode] == 0:
                return True
            
            visited[currentNode] = True
            
            lnode = currentNode - arr[currentNode]
            unode = currentNode + arr[currentNode]
            
            if lnode >= 0 and  lnode not in visited:
                q.append(lnode)
                
            if unode < len(arr) and unode not in visited:
                q.append(unode)
        
        return False
    
        
        