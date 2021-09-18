class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        
        c1, c2 = Counter(nums1), Counter(nums2)
        
        for key in c1.keys():
            if key in c2:
                output.extend([key] * min(c1[key], c2[key]))
                
        return output