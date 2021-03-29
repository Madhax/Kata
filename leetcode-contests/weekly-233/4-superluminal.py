class TrieNode:
    def __init__(self):
        self.cnt = 0
        self.child = [None, None]

class Solution(object):
    def countPairs(self, nums, low, high):
        """
        :type nums: List[int]
        :type low: int
        :type high: int
        :rtype: int
        """
        n = len(nums)
        m = max(max(nums), high).bit_length() # <= 15
        root = TrieNode()

        def add(num):
            curr = root
            for level in xrange(m-1, -1, -1):
                curr.cnt += 1
                c = (num >> level) & 1
                if curr.child[c] is None:
                    curr.child[c] = TrieNode()
                curr = curr.child[c]
            curr.cnt += 1

        def query(num, lim):
            curr = root
            r = 0
            for level in xrange(m-1, -1, -1):
                a = (num >> level) & 1
                b = (lim >> level) & 1
                if b and curr.child[a]:
                    r += curr.child[a].cnt
                curr = curr.child[a^b]
                if curr is None: break
            if curr:
                r += curr.cnt
            return r

        for i in nums:
            add(i)
        def f(lim):
            r = sum(query(i, lim) for i in nums)
            return (r - n) // 2
        return f(high) - f(low-1)