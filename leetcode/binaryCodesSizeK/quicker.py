class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k - 1 + 2 ** k:
            return False
        remaining = 2 ** k
        exist = set()
        for i in range(len(s) - k, -1, -1):
            if s[i:(i + k)] not in exist:
                remaining -= 1
                exist.add(s[i:(i + k)])
            if i < remaining:
                return False
            if remaining == 0:
                return True
        