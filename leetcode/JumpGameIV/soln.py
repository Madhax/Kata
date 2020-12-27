from collections import deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        mirrors = {}
        
        for index, val in enumerate(arr):
            if val not in mirrors:
                mirrors[val] = [index]
            else:
                mirrors[val].append(index)
                
        
        visited = set()
        bfsQueue = deque()
        visitedMirror = set()
        def bfs():
            nonlocal mirrors, arr, visited, bfsQueue, visitedMirror
            
            while len(bfsQueue):
                work = bfsQueue.popleft()
                
                if work[0] == len(arr) - 1:
                    return work[1]
                
                if 0 < work[0] and work[0]-1 not in visited:
                    bfsQueue.append([work[0]-1, work[1]+1])
                    visited.add(work[0]-1)
                    
                if work[0] < len(arr)-1 and work[0]+1 not in visited:
                    bfsQueue.append([work[0]+1, work[1]+1])
                    visited.add(work[0]+1)
                    
                if arr[work[0]] not in visitedMirror:
                    visitedMirror.add(arr[work[0]])
                    for i in mirrors[arr[work[0]]]:
                        if i == work[0]:
                            continue

                        if i in visited:
                            continue

                        bfsQueue.append([i, work[1]+1])
                        visited.add(i)
                    
            print("impossible")
            return float("inf")
                
                
        bfsQueue.append([0, 0])
        return bfs()
            