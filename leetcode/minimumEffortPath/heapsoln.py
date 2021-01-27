class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        boundary = [(0,0,0)]
        visited = set()
        ans = 0
        todo = []
        while True:
            if todo:
                a, i, j = todo.pop()
            else:
                a, i, j = heapq.heappop(boundary)
                ans = a
            if (i,j) == (m-1,n-1):
                return ans
            for x, y in ((i,j-1),(i-1,j),(i+1,j),(i,j+1)):
                if 0 <= x < m and 0 <= y < n:
                    if (x,y) not in visited:
                        d = abs(heights[x][y] - heights[i][j])
                        if d <= ans:
                            todo.append((d,x,y))
                        else:
                            heapq.heappush(boundary, (d,x,y))
            visited.add((i,j))