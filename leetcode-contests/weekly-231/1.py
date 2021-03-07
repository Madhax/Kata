class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "1" * s.count("1") in s