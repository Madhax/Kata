class Solution:
    def solve(self, requests, k):
        # calculate the earliest and latest visit times for user k.
        # return all requests that overlap with this interval.
        ks = sorted(s for s, e in requests)[k]
        ke = sorted(e for s, e in requests)[k]
        print(ks)
        print(ke)
        return [i for i, (s, e) in enumerate(requests) if not (ke < s or e < ks)]
