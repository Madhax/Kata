from math import inf


class Solution:
    def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
        n = len(boxes)
        f = [inf] * (n + 1)
        f[0] = 1

        lc = lw = 0
        for i in range(1, n + 1):
            lc += 1
            lw += boxes[i - 1][1]
            if lc > maxBoxes or lw > maxWeight:
                w = c = 0
                mc = mw = 0
                r = 1
                t = 0
                for j in reversed(range(i)):
                    c += 1
                    w += boxes[j][1]
                    if c > maxBoxes or w > maxWeight:
                        break

                    if t != boxes[j][0]:
                        r += 1
                        t = boxes[j][0]

                    if r + f[j] < f[i]:
                        f[i] = r + f[j]
                        mc = c
                        mw = w
                lc = mc
                lw = mw
            else:
                if i > 1 and boxes[i - 1][0] == boxes[i - 2][0]:
                    f[i] = f[i - 1]
                else:
                    f[i] = f[i - 1] + 1

        return f[n]
