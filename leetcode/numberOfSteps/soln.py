class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0:
            return 0
       
        if num % 2 == 0:
            return 1 + self.numberOfSteps(num/2)
        else:
            return 1 + self.numberOfSteps(num-1)

[[4,2,1],[1,4,1],[5,4,0],[2,5,0]]

5+4+3+2+1


cccc

1 + 1 + 2 + 4


1
2
3
4

1 + 3 + 3


2*3 = 6 // 2 = 3