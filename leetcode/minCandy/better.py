class Solution:
    def candy(self, ratings: List[int]) -> int:
        last = -1
        level = 0
        run = 1
        total = 0
        for rating in ratings:
            if rating > last:
                if run == 1:
                    level += 1
                else:
                    level = 2
                run = 1
                total += level
            elif rating == last:
                run = 1
                level = 1
                total += 1
            else:
                total += run
                run += 1
                if (level < run):
                    total += 1
            last = rating
        return total