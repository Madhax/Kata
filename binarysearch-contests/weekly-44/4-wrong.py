class Solution:
    def solve(self, s, target):
        
        best = math.inf
        def dfs(splitIndex, substring, curSum):
            nonlocal target, best
            #print(splitIndex, substring, curSum, target, best)
            if splitIndex > 0 and abs(curSum+int(substring[0:splitIndex]) - target) > best:
                #print("end2")
                return

            if substring == "" or splitIndex == len(substring):
                #print("end1")
                if len(substring) > 0:
                    curSum += int(substring)

                if abs(curSum-target) < best:
                    best = abs(curSum-target)

                return
        
            #split here, add to cursum
            if splitIndex > 0:
                element = substring[0:splitIndex]
                #print(element)
                curNum = int(element)
                dfs(0, substring[splitIndex:], curSum + curNum)

            if splitIndex < 4:
                dfs(splitIndex+1, substring, curSum)

            #continue


        dfs(0, s, 0)

        return best