class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        aLen = 0
        x = 0
        while x < len(asteroids) - 1:
            if asteroids[x] > 0 and asteroids[x+1] < 0:
                if abs(asteroids[x]) > abs(asteroids[x+1]):
                    #keep left
                    asteroids.pop(x+1)
                elif abs(asteroids[x]) < abs(asteroids[x+1]):
                    #keep right
                    asteroids.pop(x)
                    if x > 0:
                        x -= 1
                else:
                    asteroids.pop(x)
                    asteroids.pop(x)
                    if x > 0:
                        x -= 1
                    #destroy both
            else:
                x += 1
                   
        return asteroids
