class Solution: # bidirectional, best 368 ms
    """
    https://leetcode.com/problems/jump-game-iv/discuss/853365/No-DP-Faster-Bidirectional-BFS-with-explanation
    """
    def minJumps(self, array):
        length = len(array)
        if len(set(array)) == length: return length - 1
        if array[0] == array[-1]: return 1

        _map = defaultdict(list) # connection map
        for i, val in enumerate(array): _map[val].append(i)

        step, curs, other = 0, {0}, {length - 1}
        while curs:
            # choose smaller side
            if len(curs) > len(other): curs, other = other, curs

            step, thisLevel = step + 1, set()
            for i in curs:
                # add backward and forward moves into current jumping space
                # make the same operation accomplished in only one loop
                for j in (i + 1, i - 1):
                    if 0 < j < length: _map[array[i]].append(j)

                for j in _map[array[i]]:
                    if j in other: return step
                    else: thisLevel.add(j)
                del _map[array[i]]

            # update current side for next round          
            curs = thisLevel