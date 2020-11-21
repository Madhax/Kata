class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        pivotIndex = -1
        #logarithmic search with test if pivot found
       
        #find pivot?
        """
        find pivot in logarithmic time
        find target across range in logarithmic time = 2 log n complexity
       
        i[-1] <= i[0]
        i[mid] >  i[-1] iff  <=mid is pivot
       
        when is it a pivot?
        i[0] < i[pivot] > i[pivot+1] < i[-1]
       
        """
        def findPivot(nums, lowerBound, upperBound):
           
            mid = ((upperBound-lowerBound) // 2) + lowerBound
           
            if mid < len(nums)-1 and nums[mid] > nums[mid+1]:
                return mid
           
            elif nums[mid] == nums[-1] == nums[mid-1] and lowerBound != mid:
                return max(findPivot(nums, lowerBound, mid), findPivot(nums, mid, upperBound))
           
            elif nums[mid] <= nums[-1] and lowerBound != mid:
                return findPivot(nums, lowerBound, mid)
               
            elif lowerBound != mid:
                return findPivot(nums, mid, upperBound)
               
            return -1
       
        def binarySearch(nums, lowerBound, upperBound, target):
            mid = ((upperBound-lowerBound) // 2) + lowerBound
           
            if nums[mid] == target:
                return mid
           
            elif nums[mid] < target and lowerBound != mid:
                return binarySearch(nums, mid, upperBound, target)
           
            elif lowerBound != mid:
                return binarySearch(nums, lowerBound, mid, target)
           
            return -1
       
       
        #print(findPivot(nums, 0, len(nums)))
        if len(nums) == 0:
            return False
       
        pivotIndex = findPivot(nums, 0, len(nums))
        #print(pivotIndex)
       
        if pivotIndex == -1:
            #search all
            return binarySearch(nums, 0, len(nums), target)
       
        if nums[pivotIndex+1] <= target <= nums[-1]:
            return binarySearch(nums, pivotIndex+1, len(nums), target)
           
        else:
            #print("here")
            return binarySearch(nums, 0, pivotIndex+1, target)
         
        return True