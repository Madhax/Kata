from bisect import bisect_left, bisect_right
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        target = goal
        def gen(lst):
            ans = [0]
            for val in lst:
                new_ans = []
                for cur_sum in ans:
                    new_ans.append(cur_sum)
                    new_ans.append(cur_sum+val)
                ans = new_ans
            return ans
        
        half1 = nums[:len(nums)//2]
        half2 = nums[len(nums)//2:]
        half1 = gen(half1)
        half2 = gen(half2)
        half2.sort()
        ans = float('inf')
        for val in half1:
            i1 = bisect_right(half2, target-val)
            v1 = float('inf')
            if i1:
                v1 = half2[i1-1]
            i2 = bisect_left(half2, target-val)
            v2 = float('inf')
            if i2 != len(half2):
                v2 = half2[i2]
            ans = min(ans, abs(target-val-v1), abs(target-val-v2))
        return ans