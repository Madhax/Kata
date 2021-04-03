class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def countDigits(s):
            zeroes, ones = 0, 0
            for x in s:
                if x == "0":
                    zeroes += 1
                elif x == "1":
                    ones += 1
                   
            return (zeroes, ones)
       
        zos = []
        for cand in strs:
            zos.append(countDigits(cand))    
   
        @functools.cache
        def dp(index, z, o):
            nonlocal zos
            if index == len(zos):
                return 0
           
            if z == 0 and o == 0:
                return 0
           
            best = 0
            best =  max(best, dp(index+1, z, o))
            if zos[index][0] <= z and zos[index][1] <= o:
                best = max(best, 1 + dp(index+1, z - zos[index][0], o - zos[index][1]))
               
            return best
           
           
        return dp(0, m, n)
           
        """
        output = 0
        for cand in strs:
            (z, o) = countDigits(cand)
            if z <= m and o <= n:
                output += 1
        return output
        """
