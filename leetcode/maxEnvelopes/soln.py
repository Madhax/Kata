class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        lis = []
        for x, y in sorted(envelopes, key=lambda x: (x[0], -x[1])):
            low = bisect.bisect_left(lis, y)
            if low < len(lis):
                lis[low] = y
            else:
                lis.append(y)
        return len(lis)

