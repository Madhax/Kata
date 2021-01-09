class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        q = [(0,0,0)] # cost,i,j
        seen = set()
        while q:
            cost,i,j=heapq.heappop(q)
            if (i,j)==(len(heights)-1,len(heights[0])-1):
                return cost
            if (i,j) in seen:
                continue
            seen.add((i,j))
            for ni,nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if not 0<=ni<len(heights) or not 0<=nj<len(heights[0]):
                    continue
                if (ni,nj) in seen:
                    continue
                # whats the cost?
                price=abs(heights[i][j]-heights[ni][nj])
                heapq.heappush(q, (max(cost,price),ni,nj))
        return -1
