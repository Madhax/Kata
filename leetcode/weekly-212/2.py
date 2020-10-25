class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArithmetic(l):
            if len(l) <= 2:
                return True
            diff = l[1] - l[0]
           
            for x in range(1, len(l)):
                if l[x]-l[x-1] != diff:
                    return False
           
            return True
       
        output = []
        for index, (lower, upper) in enumerate(zip(l,r)):
            #print (index, lower, upper)
           
            subarray = nums[lower:upper+1]
            subarray.sort()
           
            output.append(isArithmetic(subarray))
            #print(subarray)
           
        return output
