class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        arr = [0 for _ in range(60)]
        count = 0
        for elem in time:
            arr[elem % 60] += 1
        
        for i in range(0, 31):
            if arr[i] == 0:
                continue
            elif (i == 0 or i == 30):

                count += int(arr[i] * (arr[i] - 1) / 2)
            else:
                count += arr[i] * arr[60-i]
        return count