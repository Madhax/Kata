class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        N = len(mat)
        M = len(mat[0])
        
        output = [ [0 for _ in range(M)] for _ in range(N)]
        memo = defaultdict(lambda : defaultdict(lambda: None))
        
        
        def bfs(start):
            if start[0] in memo and start[1] in memo[start[0]]:
                return memo[start[0]][start[1]]
            
            q = deque([(start[0], start[1], 0)])
            seen = set()
            best = math.inf
            while q:
                
                y, x, steps = q.popleft()
                
                if steps >= best:
                    continue
                
                if mat[y][x] == 0:
                    return steps
                
                if y in memo and x in memo[y]:
                    best = min(best, memo[y][x] + steps)
                
                for c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny = y + c[0]
                    nx = x + c[1]
                    if 0 <= ny < N and 0 <= nx < M and (ny, nx) not in seen:
                        seen.add((ny,nx))
                        q.append((ny,nx,steps+1))
                        
                
            return best
                
        for y in range(N):
            for x in range(M):
                output[y][x] = bfs((y,x))
                memo[y][x] = output[y][x]
                
                
        return output