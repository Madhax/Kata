class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        d = {'a': 0, 'b':1, 'c': 2, 'd': 3, 'e': 4, 'f':5,'g':6, 'h':7}
        #print(d[coordinates[0]]+1, coordinates[1])
        return (d[coordinates[0]]+1) % 2 + int(coordinates[1]) % 2 == 1