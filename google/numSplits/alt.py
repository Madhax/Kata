class Solution:
    def numSplits(self, s: str) -> int:
        # naive: check each position and count the unique letters
        # speed up counting unique time using a dictionary
        counts = {}
        for letter in s:
            counts[letter] = counts.get(letter, 0) + 1
        left, right = 0, len(counts.keys())
        seen = set()
        good = 0
        for letter in s:
            if letter not in seen:
                left += 1
                seen.add(letter)
            counts[letter] -= 1
            if counts[letter] == 0:
                del counts[letter]
                right -= 1
            if left == right:
                good += 1
        return good