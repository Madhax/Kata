class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        qidx = sorted(range(len(queries)), key = lambda qid : queries[qid][1])
        ans = [-1 for _ in range(len(queries))]
        qid = 0
        nid = 0
        trie = {}
        
        def get_bits(n):
            bits = []
            for _ in range(32):
                bits.append(n&1)
                n >>= 1
            return bits[::-1]
        
        def add_trie(n):
            bits = get_bits(n)
            cur = trie
            for b in bits:
                if b not in cur:
                    cur[b] = {}
                cur = cur[b]
            cur[-1] = n
            
        while qid < len(queries):
            x, m = queries[qidx[qid]] # get next query
            while nid < len(nums) and nums[nid] <= m:
                # add nid
                add_trie(nums[nid])
                nid += 1
            # now process query
            xb = get_bits(x)
            cur = trie
            if len(cur) > 0:
                for b in xb:
                    if b == 0: # take 1 if we can
                        if 1 in cur:
                            cur = cur[1]
                        else:
                            cur = cur[0]
                    elif b == 1: # take 0 if we can
                        if 0 in cur:
                            cur = cur[0]
                        else:
                            cur = cur[1]
                res = cur[-1]
                ans[qidx[qid]] = res ^ x
            else:
                ans[qidx[qid]] = -1
        
            qid += 1
        return ans
