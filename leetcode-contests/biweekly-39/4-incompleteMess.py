class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        uniques = set(nums)
        quantities = []
        
        for unique in uniques:
            cnt = nums.count(unique)
            #quantities[unique] = cnt
            quantities.append(cnt)
            
        totalQuantity = sum(quantity)

        quantity.sort(reverse=True)
        quantities.sort(reverse=True)
        
        #print(quantities)
        #print(totalQuantity)
        
        #sanity 
        
        for q in quantity:
            found = False
            for v in quantities:
                if v >= q:
                    found = True
                    break
                        
            if found == False: 
                return False
            
            
        #return False
        def dfs(currentQuantity):
            nonlocal quantities, totalQuantity, quantity
            
            if currentQuantity == totalQuantity:
                return True
            
            
            for x in range(len(quantity)):
                if quantity[x] == 0:
                    continue
                    
                qval = quantity[x]
                for y in range(len(quantities)):
                    if quantities[y] == 0:
                        continue
                        
                    avail = quantities[y]
                    if qval <= avail:
                        quantity[x] = 0
                        quantities[y] -= qval
                        
                        ret = dfs(currentQuantity+qval)
                        
                        if ret == True:
                            return True
                        
                        quantity[x] = qval
                        quantities[y] += avail
            
            
            return False
        
        return dfs(0)
        
        """
        working = quantity.copy()
        
        for val in quantity:
            if val in quantities:
                quantities.remove(val)
                working.remove(val)
        """
        
            