class Solution:
    def dist(self, x1, y1, x2, y2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
       
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius
       
        self.lbx = self.x_center - self.radius
        self.ubx = self.x_center + self.radius
       
        self.lby = self.y_center - self.radius
        self.uby = self.y_center + self.radius
       
    def randPoint(self) -> List[float]:
       
        notValid = True
        while notValid:
            y = random.random() * (self.uby - self.lby) + self.lby
            x = random.random() * (self.ubx - self.lbx) + self.lbx
           
            if self.radius > self.dist(x, y, self.x_center, self.y_center):
                #print(x, y,self.dist(x, y, self.x_center, self.y_center))
                return [x,y]
           


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()