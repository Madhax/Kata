class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        num_flower = sum(flowerbed)
        bed_len = len(flowerbed)
        
        if (num_flower+n) > (bed_len+1)//2:
            return False
        else:
            count = 0
            for i in range(bed_len):
                if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0)  and (i==bed_len-1 or flowerbed[i+1]==0):
                    flowerbed[i]=1
                    count+=1
                    
                if count>=n:
                    return True
            return count>=n