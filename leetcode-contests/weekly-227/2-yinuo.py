
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        arr = [a,b,c]
        arr.sort()
        ans = 0
        while arr[1] > 0:
            ans += 1
            arr[-1] -= 1
            arr[1] -= 1
            arr.sort()
        return ans