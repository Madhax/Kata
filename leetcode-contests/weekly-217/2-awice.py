class Solution(object):
    def mostCompetitive(self, A, K):
        stack = []
        to_remove = len(A) - K
        for i, x in enumerate(A):
            while stack and x < stack[-1] and to_remove:
                to_remove -= 1
                stack.pop()
            stack.append(x)
        while len(stack) > K:
            stack.pop()
        return stack