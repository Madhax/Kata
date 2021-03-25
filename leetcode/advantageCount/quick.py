class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
      idx = list(range(len(B)))
      idx.sort(key = lambda i: B[i])
      A.sort()
      res = [-1] * len(A)
      start, end = 0, len(B) - 1
      # iterate through sorted A and B
      # if a can cover b, then correspond b with a
      # if a cannot, correspond a with largest of b
      for a in A:
        if a > B[idx[start]]:
          res[idx[start]] = a
          start += 1
        else:
          res[idx[end]] = a
          end -= 1
      return res