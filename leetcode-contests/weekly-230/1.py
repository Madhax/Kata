class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        if ruleKey == "color":
            ruleIndex = 1
        elif ruleKey == "type":
            ruleIndex = 0
        elif ruleKey == "name":
            ruleIndex = 2
        cnt = 0
        for item in items:
            if item[ruleIndex] == ruleValue:
                cnt += 1
        return cnt
            