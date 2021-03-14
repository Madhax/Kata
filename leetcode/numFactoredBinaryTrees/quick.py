class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 1000000007
        arr = sorted(set(arr))
        table = {num : 1 for num in arr}
        
        for num in arr[1:] :
            for d in arr[:bisect.bisect(arr ,int(sqrt(num)))] :
                if num / d in table :
                    table[num] += table[d] * table[num / d] if d == num / d else table[d] * table[num / d] * 2
            table[num] %= mod
            
        return sum(table.values()) % mod