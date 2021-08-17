class NumArray:

    def __init__(self, nums: List[int]):
        self.l = len(nums)
        self.tree = [0] * self.l + nums
        for i in range(self.l - 1, 0, -1):
            self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]

    def sumRange(self, left: int, right: int) -> int:
        m = self.l + left
        n = self.l + right

        res = 0
        
        while m <= n:
            if m & 1:
                res += self.tree[m]
                m += 1
            
            m >>= 1

            if n & 1 == 0:
                res += self.tree[n]
                n -= 1

            n >>= 1

        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)