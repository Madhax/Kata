
class Solution:
    def recursor(self, target, order, index):
        for i, x in enumerate(self.candidates[index :]):
            if target >= 2 * x:
                self.recursor(target - x, order + [x], index + i)
            elif x == target:
                self.ans.append(order + [x])
            elif x > target:
                break

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.candidates = sorted(candidates)
        self.recursor(target, [], 0)
        return self.ans
        