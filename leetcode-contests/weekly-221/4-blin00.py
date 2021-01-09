#!/opt/python3.9/bin/python3

from bisect import *
from collections import *
from functools import *
from heapq import *
from typing import *
import sys

INF = float('inf')

T = lambda: defaultdict(T)

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)
        M = len(queries)

        trie = T()

        def bignum_dp(n):
            return bin(n)[2:].zfill(32)

        nums.sort()
        queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        result = [None] * len(queries)
        last = 0
        
        for query_idx, (x, limit) in queries:
            while last < len(nums) and nums[last] <= limit:
                n = nums[last]
                reduce(dict.__getitem__, bignum_dp(n), trie)['#'] = n
                last += 1
            guh = bignum_dp(x)
            r = 0
            node = trie
            for c in guh:
                c = int(c)
                wanted = c ^ 1
                if str(wanted) in node:
                    node = node[str(wanted)]
                elif str(wanted ^ 1) in node:
                    node = node[str(wanted ^ 1)]
                else:
                    node = None
                    break
            if node is None:
                result[query_idx] = -1
            else:
                result[query_idx] = node['#'] ^ x
        return result
