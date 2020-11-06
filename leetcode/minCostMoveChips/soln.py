class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odds = 0
        evens = 0
        for coin in position:
            if coin % 2 == 1:
                odds += 1
            else:
                evens += 1

        if odds > evens:
            return evens
        else:
            return odds
        