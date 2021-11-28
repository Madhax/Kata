class Solution:
    def maxProduct(self, S: str) -> int:
        N = len(S)
        def manachers(S):
            A = '@#' + '#'.join(S) + '#$'
            Z = [0] * len(A)
            center = right = 0
            for i in range(1, len(A) - 1):
                if i < right:
                    Z[i] = min(right - i, Z[2 * center - i])
                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                    Z[i] += 1
                if i + Z[i] > right:
                    center, right = i, i + Z[i]
            return Z
        A = manachers(S)
        B = A[2::2]
        B.pop()
        
        def make(B):
            furthest = 0
            ans = [0] * len(B)
            for i, length in enumerate(B):
                j = (length >> 1) + i
                ans[j] = max(ans[j], length)
            
            for j in range(len(ans) - 2, -1, -1):
                ans[j] = max(ans[j], ans[j+1] - 2)
            # print("PRE", ans)
            for i in range(1, len(ans)):
                ans[i] = max(ans[i], ans[i-1])
            return ans
        
        # print("B", B)
        left = make(B)
        right = make(B[::-1])[::-1]
        
        # print(left)
        # print(right)
        # eve dhkbdhntnhdbkhd 45
        # "ggbswiymmlevedhkbdhntnhdbkhdevelmmyiwsbgg"
        ans = 0
        for i in range(len(left) - 1):
            ans = max(ans, left[i] * right[i + 1])
        return ans
