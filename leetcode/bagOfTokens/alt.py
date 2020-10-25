class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        if not tokens or P < tokens[0]:
            return 0
        score = 0
        left, right = 0, len(tokens) - 1
        while left <= right:
            if P >= tokens[left]:
                P -= tokens[left]
                left += 1
                score += 1
            else:
                if right - left > 1:
                    P += tokens[right]
                    right -= 1
                    score -= 1
                else:
                    break
        return score
            