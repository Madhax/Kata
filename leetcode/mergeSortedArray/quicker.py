class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #nums1[len(nums1)-len(nums2):] = nums2
        #nums1.sort()
        temp = [0]*(m+n)
        
        i,j = 0,0
        cursor = 0
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                temp[cursor] = nums1[i]
                i+=1
                cursor+=1
            else:
                temp[cursor] = nums2[j]
                j+=1
                cursor+=1
                
        while i<m:
            temp[cursor] = nums1[i]
            i+=1
            cursor+=1
            
        while j<n:
            temp[cursor] = nums2[j]
            j+=1
            cursor+=1
            
        for i in range(m+n):
            nums1[i] = temp[i]