class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        """
        @lru_cache(maxsize=100000)
        def dpmin(i, j):
            
            if i > j:
                return math.inf 
            
            if i == j:
                return nums[i]
            
            #print(i,j)
            num = min(nums[i], nums[j])
            
            return min(num, dpmin(i+1, j), dpmin(i, j-1))

        """
        
        INT_MAX = sys.maxsize; 


        def minVal(x, y) : 
            return x if (x < y) else y;  


        def getMid(s, e) : 
            return s + (e - s) // 2;  


        def RMQUtil( st, ss, se, qs, qe, index) : 

            if (qs <= ss and qe >= se) : 
                return st[index];  

            if (se < qs or ss > qe) : 
                return INT_MAX;  


            mid = getMid(ss, se);  
            return minVal(RMQUtil(st, ss, mid, qs,  
                                  qe, 2 * index + 1),  
                          RMQUtil(st, mid + 1, se, 
                                  qs, qe, 2 * index + 2));  


        def RMQ( st, n, qs, qe) :  
            if (qs < 0 or qe > n - 1 or qs > qe) : 

                print("Invalid Input");  
                return -1;  

            return RMQUtil(st, 0, n - 1, qs, qe, 0);  


        def constructSTUtil(arr, ss, se, st, si) : 
            if (ss == se) : 

                st[si] = arr[ss];  
                return arr[ss];  


            mid = getMid(ss, se);  
            st[si] = minVal(constructSTUtil(arr, ss, mid, 
                                            st, si * 2 + 1), 
                            constructSTUtil(arr, mid + 1, se, 
                                            st, si * 2 + 2));  

            return st[si];  


        def constructST( arr, n) : 
            x = (int)(ceil(log2(n)));  

            max_size = 2 * (int)(2**x) - 1;  

            st = [0] * (max_size);  

            constructSTUtil(arr, 0, n - 1, st, 0);  

            return st;  


        i = 0
        j = len(nums) - 1
        
        best = -math.inf
        
        n = len(nums)
        st = constructST(nums, n);  
        
        def myFind(l, element, start, end):
            
            lastIndex = -1
            
            
            while start <= end:
                #print(l[start])
                if l[start] == element:
                    lastIndex = start
                    
                start += 1
            
            if lastIndex == -1:
                return math.inf
            return lastIndex
        
        #binarysearch on values?
        while i <= k <= j:
            curMin = RMQ(st, n, i, j)
            best = max(best, curMin * int(j-i+1))
                
            if i == k == j:
                break
             
            startindex = myFind(nums, curMin, i, k) #nums.index(curMin, i, k)

            try:
                #print(n, rnums.index(curMin, n-j))
                endindex = nums.index(curMin, k, j+1)
            except:
                endindex = -1
            
            #print(curMin, startindex, endindex)
            if startindex <= k or (endindex) > k:
                if startindex <= k:
                    i = startindex + 1
                
                
                if endindex > k:
                    j = endindex - 1
                    
            else:
                break
                
            if i == startindex and j == endindex:
                break
        
        return best