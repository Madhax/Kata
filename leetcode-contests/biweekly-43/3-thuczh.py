class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        a = [0] * (n * 2 - 1)
        c = [True] * (n + 1)
        c[1] = 1

        def work(k):
            if k == n * 2 - 1:
                return True
            if a[k] > 0:
                return work(k + 1)
            for i in range(n, 0, -1):
                if c[i]:
                    if i == 1:
                        a[k] = 1
                        c[i] = False
                        if work(k + 1):
                            return True
                        c[i] = True
                        a[k] = 0
                    elif i + k < 2 * n - 1 and a[i + k] == 0:
                        a[k] = i
                        a[i + k] = i
                        c[i] = False
                        if work(k + 1):
                            return True
                        c[i] = True
                        a[k] = 0
                        a[i + k] = 0
            return False

        work(0)

        return a
