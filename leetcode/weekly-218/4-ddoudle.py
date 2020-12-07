class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        if max(cnt.values()) > k:
            return -1
        if k == 1:
            return 0
        k = len(nums) // k
        nums.sort()
        nums = map(str, nums)
        nums = ' '.join(nums)
        # print(nums)
        @lru_cache(None)
        def helper(arr, k):
            # print(arr, k)
            arr = list(map(int, arr.split(' ')))
            # print(arr)
            if len(arr) == k:
                if len(set(arr)) == len(arr):
                    return max(arr) - min(arr)
                else:
                    return float('inf')
            else:
                mn = float('inf')
                for comb in combinations(arr, k):
                    # print(arr, comb)
                    if len(set(comb)) == len(comb):
                        newarr = []
                        idx = 0
                        for a in arr:
                            if idx < len(comb) and a == comb[idx]:
                                idx += 1
                            else:
                                newarr.append(a)
                        newarr = map(str, newarr)
                        newarr = ' '.join(newarr)
                        mn = min(mn, max(comb) - min(comb) + helper(newarr, k))
                return mn
        res = helper(nums, k)
        if res == float('inf'):
            return -1
        return res