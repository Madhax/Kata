class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                r = s.pop()
                l = s.pop()
                if t == "+":
                    s.append(l + r)
                elif t == "-":
                    s.append(l - r)
                elif t == "*":
                    s.append(l * r)
                elif t == "/":
                    s.append(int(l / r))
            else:
                s.append(int(t))
        return s.pop()