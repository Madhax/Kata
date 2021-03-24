class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
       
        numCounter = Counter(arr)
        uniqueNums = sorted(list(set(arr)))

        ctr = 0
        for i in range(0, len(uniqueNums)):
            num1 = uniqueNums[i]
            if num1 > target:
                break
            for j in range(i, len(uniqueNums)):
                num2 = uniqueNums[j]
                num3 = target - num1 - num2
                if num3 < num2:
                    continue
                if num3 in uniqueNums:
                    #print(num1, num2, num3)
                    choose = Counter([num1, num2, num3])                    
                    numChoices = 1
                    for key in choose.keys():
                        numChoices *= math.comb(numCounter[key], choose[key])
               
                    ctr += numChoices
        return ctr % (10**9 + 7)