class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        case = s.split(" ")
        return " ".join(case[:k])