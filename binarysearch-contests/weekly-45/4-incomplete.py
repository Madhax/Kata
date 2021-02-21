from collections import Counter
class Solution:
    def solve(self, digits, lower):

        if len(digits) > len(lower):
            lower = ("0" * (len(digits) - len(lower))) + lower

        digits = list(map(int, digits))
        lower = list(map(int, lower))

        d = Counter()
        for digit in digits:
            d[int(digit)] += 1

        #print(d)
        #highest value digits that fulfill the requirements

        
        #minimize using maximal digits
        #@functools.cache
        def minimize(index, MustBeGreater):
            nonlocal lower, d

            if index == len(lower) and MustBeGreater:
                return math.inf

            elif index == len(lower):
                return 0

            ans = math.inf

            for x in range(9, -1, -1):
                if x < int(lower[index]) and MustBeGreater:
                    break

                if d[x] > 0:
                    d[x] -= 1
                    tmp = MustBeGreater
                    if x > lower[index]:
                        MustBeGreater = False

                    ans = min(ans, (x * (10**(len(lower)-index-1))) + minimize(index+1, MustBeGreater))
                    MustBeGreater = tmp
                    
                    d[x] += 1

            return ans

        minVal = minimize(0, True)

        for c in str(minVal):
             d[int(c)] -= 1

        prefix = []
        for c in d.keys():
            prefix.extend([str(c) * d[c]])

        prefix.sort()
        ret = str(int("".join(prefix) + str(minVal)))
        return ret