class Solution:
    def calculate(self, s: str) -> int:
        stack, num, ops = [], 0, '+'  # don't need i
        s = s + '+'
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in {'+', '-', '*', '/'}:
                if ops == '+':
                    stack.append(num)
                elif ops == '-':
                    stack.append(-num)
                elif ops == '*':
                    stack[-1] *= num
                elif ops == '/':
                    stack[-1] = int(float(stack[-1]) / num)
                    # stack[-1]=stack[-1]//num if stack[-1]>=0 else ceil(stack[-1]/num)
                num, ops = 0, c

        return sum(stack)
        return sum(stack