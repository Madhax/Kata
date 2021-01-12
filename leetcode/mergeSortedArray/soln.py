class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #cheat
        """
        newarray = nums1[:len(nums1)-len(nums2)] + nums2
        newarray.sort()
        nums1[:] = newarray
        """
       
        #2ptr
        num1end = len(nums1)-1
        num2end = len(nums2)-1
        num1ptr = num1end - num2end - 1
       
        while num1end >= 0 or num2end >= 0:
            #print(num1ptr, num1end, num2end)
            if num2end < 0 or (num1ptr >= 0 and nums1[num1ptr] > nums2[num2end]):
                #print("!", nums1[num1end], nums1[num1ptr])
                nums1[num1end] = nums1[num1ptr]
                num1end -= 1
                num1ptr -= 1
               
            else:
                #print("#", nums1[num1end], nums2[num2end])
                nums1[num1end] = nums2[num2end]
                num1end -= 1
                num2end -= 1
               
            #num1[num1end]