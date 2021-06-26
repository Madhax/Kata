class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        

        # implement Binary Index Tree
        def update (index, value, tree, size):
            index+=1
            while index < size:
                tree[index] += value
                index += index & -index
                
        def query(index, tree):
            res = 0
            while index >= 1:
                res += tree[index]
                index -=  index & -index 
            return res
        
       
        
        offset = 10**4
        size = 2*10**4 +2
        
        tree = [0] * size
        result = []
        for num in reversed(nums):
            smaller_count = query(num+offset, tree)
            result.append(smaller_count)
            update(num+offset, 1, tree, size)
        return reversed(result)
     