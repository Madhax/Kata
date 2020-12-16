class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        height = q
        side = 1
        up = 0
        while True:
            while height % p:
                height += q
                side = (side + 1) % 2
                #print(height, side)
           
            up = (height//p) % 2
            if not (side == 0 and up == 0):
                break
            else:
                height += q
                side = (side + 1) % 2
            #print(up)
           
        #print(up, side, height)
        if side == 0 and up == 1:
            return 2
       
        elif side == 1 and up == 1:
            return 1
       
        else:
            return 0