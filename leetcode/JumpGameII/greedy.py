class Solution:
    # https://leetcode.com/problems/jump-game-ii/discuss/18014/Concise-O(n)-one-loop-JAVA-solution-based-on-Greedy
    def jump(self, n: List[int]) -> int:
        currEnd = currFarthest = jump = 0
        l = len(n)
        for i in range(l-1):
            currFarthest = max(currFarthest, i + n[i])
            if i == currEnd:
                jump+=1
                currEnd = currFarthest
            
        return jump
            