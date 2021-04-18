class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort(reverse=True)
        output = 0
        while len(costs) > 0 and coins > 0:
            if coins >= costs[-1]:
                output += 1
                coins -= costs[-1]
                costs.pop()
            else:
                break
                
        return output