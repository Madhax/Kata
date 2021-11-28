class Robot:

    def __init__(self, width: int, height: int):
        self.direction = (0,1)
        self.position = [0,0]
        self.w = width
        self.h = height
        
        self.mod = (width*2)+((height-2)*2)
                
    def move(self, num: int) -> None:
        num = num % self.mod
        if num == 0:
            num += self.mod
        
        while num > 0:
            #print(self.direction, self.position, num)
            if self.direction == (0,1):
                if self.position[1] == self.w-1:
                    self.direction = (1, 0)
                else:
                    canMove = min(self.w - self.position[1] - 1, num)
                    num -= canMove
                    self.position[1] += canMove
                
                
            elif self.direction == (1,0):
                if self.position[0] == self.h-1:
                    self.direction = (0,-1)
                else:
                    canMove = min(self.h - self.position[0]-1, num)
                    num -= canMove
                    self.position[0] += canMove
                
                
            elif self.direction == (0,-1):
                if self.position[1] == 0:
                    self.direction = (-1, 0)
                else:
                    canMove = min(self.position[1], num)
                    num -= canMove
                    self.position[1] -= canMove
                
                
            elif self.direction == (-1,0):
                if self.position[0] == 0:
                    self.direction = (0,1)
                else:
                    canMove = min(self.position[0], num)
                    num -= canMove
                    self.position[0] -= canMove
                
                

    def getPos(self) -> List[int]:
        return [self.position[1], self.position[0]]

    def getDir(self) -> str:
        if self.direction == (0,1):
            return "East"
        elif self.direction == (1,0):
            return "North"
    
        elif self.direction == (0,-1):
            return "West"
        
        elif self.direction == (-1, 0):
            return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.move(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
