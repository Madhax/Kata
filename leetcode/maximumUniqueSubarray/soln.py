class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        mono = deque()
        used = set()
        
        curSum = 0
        best = 0
        for num in nums:
            if num not in used:
                used.add(num)
                mono.append(num)
                curSum += num
                best = max(best, curSum)
            else:
                while True:
                    val = mono.popleft()
                    if val == num:
                        mono.append(num)
                        break
                    curSum -= val
                    used.remove(val)
        
        return best
                
                