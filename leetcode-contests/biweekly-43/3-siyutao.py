from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        d = [1] * (n + 1)

        def helper(data, idx):
            if idx == 2 * n - 1:
                return data

            if data[idx] != -1:
                return helper(data, idx + 1)

            for i in range(n, 0, -1):
                # print(i)
                if d[i]:
                    if i == 1:
                        data[idx] = 1
                        d[1] -= 1
                        tmp = helper(data, idx +1)
                        if tmp:
                            return tmp
                        else:
                            d[1] += 1
                            data[idx] = -1
                    else:

                        idx2 = idx + i
                        if idx2 < len(data) and data[idx2] == -1:
                            data[idx] = i
                            data[idx2] = i
                            d[i] -= 1
                            tmp = helper(data, idx + 1)
                            if tmp:
                                return tmp
                            else:
                                d[i] += 1
                                data[idx] = -1
                                data[idx2] = -1
            return None

        return helper([-1] * (2*n-1), 0)

