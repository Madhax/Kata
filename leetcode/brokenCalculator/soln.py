class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if Y <= X:
            return X - Y
        
        if Y % 2 == 0:
            return int(self.brokenCalc(X, Y/2) + 1)
        else:
            return int(self.brokenCalc(X, Y+1) + 1)
        