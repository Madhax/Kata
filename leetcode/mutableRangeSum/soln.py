class NumArray:

    tree = [0] * (3*10**4)*2
    n = 0
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        n = self.n
        for i in range(n) :
            self.tree[n + i] = nums[i];
     
        # build the tree by calculating parents
        for i in range(n - 1, 0, -1) :
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1];

    def update(self, index: int, val: int) -> None:
        
        # set value at position p
        n = self.n
        self.tree[index + n] = val;
        index = index + n;

        # move upward and update parents
        i = index;

        while i > 1 :

            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1];
            i >>= 1;

    def sumRange(self, l: int, r: int) -> int:
        r += 1
        n = self.n
        res = 0;
     
        # loop to find the sum in the range
        l += n;
        r += n;

        while l < r :

            if (l & 1) :
                res += self.tree[l];
                l += 1

            if (r & 1) :
                r -= 1;
                res += self.tree[r];

            l >>= 1;
            r >>= 1

        return res;


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)