class Solution:  # A* search, best 376 ms
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid) - 1
        if grid[0][0] or grid[n][n]:
            return -1
        directions = [x for x in product((-1, 0, 1), repeat=2) if x != (0, 0)]

        q = [(n + 1, 1, n, n)]  # put (evaluation, step, i, j) into q
        grid[n][n] = -1  # the step of the start is 1

        while q:
            _, step, i, j = heappop(q)
            # arrive the end, return minimal step
            if (i, j) == (0, 0):
                return step
            
            for di, dj in directions:
                newI, newJ = i + di, j + dj
                # Except grid[i][j] = 1, we need to search and update
                if 0 <= newI <= n and 0 <= newJ <= n and grid[newI][newJ] < 1:
                    newStep = step + 1
                    # if we have new visit or can have fewer steps, update
                    if grid[newI][newJ] == 0 or grid[newI][newJ] < -newStep:
                        grid[newI][newJ] = -newStep  # store new minimal step
                        evaluation = max(newI, newJ) + newStep
                        heappush(q, (evaluation, newStep, newI, newJ))
        return -1