class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        iter = 0
        while iter < len(flowerbed):
            if flowerbed[iter] != 0:
                pass
            
            elif iter == 0 and iter+1 < len(flowerbed) and flowerbed[iter+1] != 1:
                flowerbed[iter] = 1
                n -= 1
                
            elif iter > 0 and iter+1 < len(flowerbed) and flowerbed[iter+1] != 1 and flowerbed[iter-1] == 0:
                flowerbed[iter] = 1
                n -= 1
            
            elif iter == len(flowerbed)-1 and flowerbed[iter-1] == 0:
                flowerbed[iter] = 1
                n -= 1
        
            if n == 0:
                return True
            
            iter += 1
        
        return n <= 0
    