class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        d = []
       
        increasing = None
        for x in nums:
            if increasing == True:
                if d[-1]  < x:
                    d.pop()
                    d.append(x)
                elif d[-1] > x:
                    d.append(x)
                    increasing = False
            elif increasing == False:
                if d[-1] > x:
                    d.pop()
                    d.append(x)
                elif d[-1] < x:
                    d.append(x)
                    increasing = True
            else:
                if len(d) and d[-1] < x:
                    d.append(x)
                    increasing = True
                elif len(d) and d[-1] > x:
                    d.append(x)
                    increasing = False
                elif len(d) == 0:
                    d.append(x)
                   
       
        return len(d)