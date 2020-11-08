from sortedcontainers import SortedList
class Solution(object):
    def createSortedArray(self, instructions):
        A = SortedList()
        count = Counter(A)
        ans = 0
        for x in instructions:
            i = A.bisect_left(x)
            left = i
            right = len(A) - left - count[x]
            ans += min(left, right)
            # print("!", left, right)
            A.add(x)
            count[x] += 1
        
        MOD = 10 ** 9 + 7
        return ans % MOD