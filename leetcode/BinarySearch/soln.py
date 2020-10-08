class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < -9999 or target > 9999:
            return -1
        
        listSize = len(nums)
        currentPosn = int(listSize/2)
        lval = 0
        rval = listSize
        while True:
            
            number = nums[currentPosn]
            #print(number, currentPosn, lval, rval)
            if number == target:
                return currentPosn
            
            if number > target:
                newPosn = int((currentPosn-lval)/2)
                #print("left", newPosn)
                if newPosn == currentPosn:
                    return -1
                
                rval = currentPosn
                currentPosn = newPosn
                continue
                
            else:
                newPosn = currentPosn + int((rval-currentPosn)/2)
                #print("right", newPosn)
                if newPosn == currentPosn:
                    return -1
                
                lval = currentPosn
                currentPosn = newPosn
                continue
            