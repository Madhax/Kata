"""
Input: arr = [4,8,12,16]
Output: 2


arr[2] < arr[3]


For i <= k < j:
    arr[k] > arr[k + 1] when k is odd, and
    arr[k] < arr[k + 1] when k is even.
    
Or, for i <= k < j:
    arr[k] > arr[k + 1] when k is even, and
    arr[k] < arr[k + 1] when k is odd.

2  , 3
[12,16]
"""
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        LT = 1
        GT = 2

        best = -math.inf
        x = 0
        idx = 0
        while idx < len(arr):
            bestcount = 1
            for state in range(1, 3):
                y = idx + 1
                while y < len(arr):
                    if state == LT and arr[y] < arr[y-1]:
                        state = GT
                        y += 1
                    elif state == GT and arr[y] > arr[y-1]:
                        state = LT
                        y += 1
                    else:
                        break

                count = y-idx
                best = max(best, count)
                bestcount = max(bestcount, count)
            idx += max(1, bestcount-1)

                
        return best if best != -math.inf else min(len(arr), 0)
    
            
            
            
            
    