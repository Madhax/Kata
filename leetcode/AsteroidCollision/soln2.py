class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for asteroid in asteroids:
            addAsteroid = True
            while s and asteroid < 0 and s[-1] > 0:
                if abs(asteroid) > s[-1]:
                    s.pop()
                    continue
                elif abs(asteroid) == s[-1]:
                    s.pop()
                addAsteroid = False
                break
               
            if addAsteroid == True:
                s.append(asteroid)
               
        return s