from collections import deque
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        
        #change significant digits to be larger or smaller
        nums1.sort()
        nums1 = deque(nums1)
        
        nums2.sort()
        nums2 = deque(nums2)
        
        
        s1 = sum(nums1)
        s2 = sum(nums2)
        ops = 0
        while s1 != s2:
            diff = abs(s1-s2)
            news1 = s1
            news2 = s2
            #print(nums1, nums2, diff)
            if s1 < s2:
                #s1 gets bigger, s2 gets smaller
                #print("s1 should increase")
                val1 = nums1[0]
                val2 = nums2[-1]
                
                if (6-val1) > (val2-1):
                    #nums1[nums1.index(val1)] = val1 + min(diff, 6-val1)
                    nums1.popleft()
                    nums1.append(val1 + min(diff, 6-val1))
                    news1 +=  min(diff, 6-val1)
                    
                else:
                    #nums2[nums2.index(val2)] = val2 - min(diff, val2-1)
                    nums2.pop()
                    nums2.appendleft(val2 - min(diff, val2-1))
                    news2 -=  min(diff, val2-1)
            else:
                val1 = nums1[-1]
                val2 = nums2[0]
                
                #print("s1 should decrease")
                #print(val1, val2)
                if (val1-1) > (6-val2):
                    #nums1[nums1.index(val1)] = val1 - min(diff, val1-1)
                    nums1.pop()
                    nums1.appendleft(val1 - min(diff, val1-1))
                    news1 -=  min(diff, val1-1)
                else:
                    nums2.popleft()
                    nums2.append(val2 + min(diff, 6-val2))
                    #nums2[nums2.index(val2)] = val2 + min(diff, 6-val2)
                    news2 +=  min(diff, 6-val2)
                    
            
            
            if news1 == s1 and news2 == s2:
                return -1
            
            s1 = news1
            s2 = news2
            
            ops += 1
        
        return ops
            