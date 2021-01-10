class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        left = 0
        right = 10 ** 10
        N = len(jobs)
        if k >= N:
            return max(jobs)

        def good(target):
            total = [0] * k
            
            def go(index):
                if index == N:
                    return True
                
                for x in range(k):
                    if (x == 0 or total[x] != total[x-1]) and total[x] + jobs[index] <= target:
                        total[x] += jobs[index]
                        if go(index + 1):
                            return True
                        total[x] -= jobs[index]
                return False
            return go(0)
        
        while left < right:
            mid = (left + right) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
                
        return left
