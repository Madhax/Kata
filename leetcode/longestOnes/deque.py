class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        q = deque()
        best = 0
        
        for val in nums:
            if val == 1:
                q.append(1)
                
            if val == 0:
                while q and k == 0:
                    if q.popleft() == 0:
                        k += 1
                        
                if k > 0:
                    k -= 1
                    q.append(0)
                        
            
            best = max(best, len(q))
    
        return best