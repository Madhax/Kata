class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        #print(matrix)
        if len(matrix) == 0:
            return []
        M, N = len(matrix), len(matrix[0])
        memo = defaultdict(dict)
       
       
        #for row in matrix:
        #    print(row)
        def bfs(ory, orx):
            ret = 0
            q = deque()
            q.append([ory,orx, matrix[ory][orx]])
            seen = set()
            seen.add((ory,orx))
            while len(q):
                (y, x, height) = q.popleft()
                #print(y, x, height)
                if y in memo:
                    if x in memo[y]:
                        ret |= memo[y][x]
               
                if y == 0 and x == N-1:
                    ret |= 3
                    break
                if x == 0 and y == M-1:
                    ret |= 3
                    break
                if x == 0 or y == 0:
                    ret |= 1
                if y == M-1 or x == N-1:
                    ret |= 2
               
                if y < M-1 and height >= matrix[y+1][x] and (y+1, x) not in seen:
                    q.append([y+1, x, matrix[y+1][x]])
                    seen.add((y+1, x))
               
                if y > 0 and height >= matrix[y-1][x] and (y-1, x) not in seen:
                    q.append([y-1, x, matrix[y-1][x]])
                    seen.add((y-1, x))
                   
                if x < N-1 and height >= matrix[y][x+1] and (y, x+1) not in seen:
                    q.append([y, x+1, matrix[y][x+1]])
                    seen.add((y, x+1))
                   
                if x > 0 and height >= matrix[y][x-1] and (y, x-1) not in seen:
                    q.append([y, x-1, matrix[y][x-1]])
                    seen.add((y, x-1))
                   
            memo[ory][orx] = ret
            return ret
           
        output = []
        #print(bfs(0,13))
       
        for y in range(0, M):
            for x in range(0, N):
                if bfs(y, x) == 3:
                    output.append([y,x])
       
           
        return output